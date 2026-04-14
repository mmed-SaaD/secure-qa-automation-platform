import os
import pytest
import re
import requests
import psycopg2
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from pathlib import Path
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from src.ui.pages.login_page import LoginPage
from src.ui.pages.inventory_page import InventoryPage
from src.ui.pages.cart_page import CartPage
from core.utils.user import User
from src.api.recipe import Recipe
from src.db.counting_cursor import CountingCursor



ENV_PATH = Path(__file__).resolve().parents[1] / ".env"
ARTIFACTS = Path(__file__).resolve().parents[1] / "artifacts"
SCREENSHOTS = ARTIFACTS / "screenshots"
VIDEOS = ARTIFACTS / "videos"
TRACES = ARTIFACTS / "traces"
load_dotenv(ENV_PATH)


@pytest.fixture(scope="session")
def api_login_token_verification(API_BASE_URL, USERNAME_API, PASSWORD_API):
    credentials = {
        "username" : USERNAME_API,
        "password" : PASSWORD_API
    }
    response =  requests.post(f"{API_BASE_URL}/auth/login" , json = credentials)
    assert response.status_code == 200, f"Something went wrong, response returned status code {response.status_code}"

    data = response.json()
    assert "accessToken" in data
    assert len(data["accessToken"]) > 0
    
    return data["accessToken"]


@pytest.fixture
def login_to_inventory_page(page, BASE_URL, USERNAME, PASSWORD) -> InventoryPage:
    login_page = LoginPage(page, BASE_URL) 
    standard_user = User(USERNAME, PASSWORD)
    login_page.open_page() 
    login_page.assert_loaded() 
    login_page.valid_login(standard_user)
    inventory_page = InventoryPage(page) 
    inventory_page.assert_list_is_loaded()
    return inventory_page

@pytest.fixture
def cart_page_with_items(login_to_inventory_page, page):
    inventory_page = login_to_inventory_page
    inventory_page.add_to_cart_from_list(1)
    inventory_page.add_to_cart_from_details(3)
    inventory_page.add_to_cart_from_list(4)
    inventory_page.add_to_cart_from_list(5)
    inventory_page.go_to_cart()
    cart_page = CartPage(page)
    cart_page.assert_loaded()
    return cart_page

@pytest.fixture
def proceed_to_checkout(cart_page_with_items):
    cart_page_with_items.checkout()

@pytest.fixture(scope="session")
def BASE_URL():
    url = os.getenv("BASE_URL")
    if not url:
        raise ValueError("BASE_URL not found in .env")
    return url

@pytest.fixture(scope="session")
def USERNAME():
    username = os.getenv("USERNAME")
    if not username:
        raise ValueError("No username found in .venv")
    return username

@pytest.fixture(scope="session")
def LOCKEDUSER():
    locked_username = os.getenv("LOCKEDUSER")
    if not locked_username:
        raise ValueError("No LOCKEDUSER found in .env")
    return locked_username

@pytest.fixture(scope="session")
def PASSWORD():
    password = os.getenv("PASSWORD")
    if not password:
        raise ValueError("No password found in .env")
    return password

@pytest.fixture(scope="session")
def FIRSTNAME():
    firstname = os.getenv("FIRSTNAME")
    if not firstname:
        raise ValueError("No firstname found in .env")
    return firstname

@pytest.fixture(scope="session")
def LASTNAME():
    lastname = os.getenv("LASTNAME")
    if not lastname:
        raise ValueError("No lastname found in .env")
    return lastname

@pytest.fixture(scope="session")
def ZIP():
    zip_code = os.getenv("ZIP")
    if not zip_code:
        raise ValueError("No ZIP found in .env")
    return zip_code

@pytest.fixture(scope="session")
def PAYMENT_INFO():
    payment_info = os.getenv("PAYMENT_INFO")
    if not payment_info:
        raise ValueError("No PAYMENT_INFO in .env")
    return payment_info

@pytest.fixture(scope="session")
def inventory_page(page):
    inventory_page = InventoryPage(page)
    return inventory_page 
    
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture
def context(browser, request):
    SCREENSHOTS.mkdir(parents=True,exist_ok=True)
    VIDEOS.mkdir(parents=True,exist_ok=True)
    TRACES.mkdir(parents=True, exist_ok=True)

    context = browser.new_context(
        #Since it expects a string 
        record_video_dir=str(VIDEOS),
        viewport={"width": 1440, "height": 900}
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context
    context.close()

@pytest.fixture
def page(context, request):
    page = context.new_page()
    yield page

    #get request.node.rep_call and if it does not exist return None
    failed = getattr(request.node, "rep_call", None) and request.node.rep_call.failed
    print(f"failed : {failed}")

    safe_name = re.sub(r"[^a-zA-Z0-9_.-]+","_", request.node.nodeid)

    if failed:
        page.screenshot(path=str(SCREENSHOTS / f"{safe_name}.png"))
        context.tracing.stop(path=str(TRACES/ f"{safe_name}.zip"))   
    else:
        context.tracing.stop()
    
    page.close()

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
#item : the test itself
#call : infos abt what is currently being executed (setup, call or teardown)

def pytest_runtest_makereport(item,call):
    #yield => to wait until pytest finishes running the test phase
    outcome = yield
    rep = outcome.get_result()
    #building a dynamic name : rep_call, rep_setup, rep_teardown
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="session")
def API_BASE_URL():
    api_base_url = os.getenv("API_BASE_URL")
    if not api_base_url:
        raise ValueError("No API_BASE_URL was found in .env")
    return api_base_url

@pytest.fixture(scope="session")
def USERNAME_API():
    username = os.getenv("USERNAME_API")
    if not username:
        raise ValueError("No USERNAME_API found in .env")
    return username

@pytest.fixture(scope="session")
def PASSWORD_API():
    password = os.getenv("PASSWORD_API")
    if not password:
        raise ValueError("No PASSWORD_API found in .env")
    return password

@pytest.fixture(scope="session")
def db_connection():
    conn = psycopg2.connect(
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD")
    )
    yield conn
    conn.close()

@pytest.fixture(scope="session")
def db_readonly_connection():
    conn = psycopg2.connect(
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_RO_USER"),
        password = os.getenv("DB_RO_PASSWORD")
    )
    yield conn
    conn.close()

@pytest.fixture(scope="session")
def db_unpriviliged_connection():
    conn = psycopg2.connect(
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_UNPRIVILIGED_USER"),
        password = os.getenv("DB_UNPRIVILIGED_PASSWORD")
    )
    yield conn
    conn.close()

@pytest.fixture(scope="function")
def db_cursor(db_connection):
    cursor = db_connection.cursor()
    yield cursor
    db_connection.rollback() #Undo any changes performed by the test
    cursor.close()

@pytest.fixture
def get_perf_test_table(db_cursor, db_connection):
    table_name = "users_perf_test"
    conn = db_connection
    cur = db_cursor
    cur.execute(f"DROP TABLE IF EXISTS {table_name};")
    cur.execute(f"""
        CREATE TABLE {table_name} (
            user_id SERIAL PRIMARY KEY,
            email TEXT NOT NULL,
            name TEXT
        );
    """)
    values = [
        (f"user{i}@gmail.com" , f"name_{i}") for i in range (0,10001)
    ]
    for value in values:
        cur.execute(f"INSERT INTO {table_name}(email, name) VALUES(%s, %s)", (value[0], value[1]))

    cur.execute(f"ANALYZE {table_name};")

    yield table_name
    cur.execute(f"DROP TABLE IF EXISTS {table_name};")

@pytest.fixture
def create_users_table(db_cursor):
    ph = PasswordHasher()
    cur = db_cursor
    table_name = "security_test_users"
    cur.execute(f"DROP TABLE IF EXISTS {table_name}")
    cur.execute(f"""
        CREATE TABLE {table_name}(
            user_id SERIAL PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        );
    """)
    users = [
        (f"user{i}__{i}", ph.hash(f"password_{i}")) for i in range (1,901)
    ]
    for user in users:
        cur.execute(f"INSERT INTO {table_name}(username, password) VALUES(%s, %s)", (user[0], user[1]))
    
    yield table_name
