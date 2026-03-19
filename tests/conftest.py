import os
import pytest
import re
from pathlib import Path
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from src.ui.pages.login_page import LoginPage
from src.ui.pages.inventory_page import InventoryPage
from src.ui.pages.cart_page import CartPage
from core.utils.user import User


ENV_PATH = Path(__file__).resolve().parents[1] / ".env"
ARTIFACTS = Path(__file__).resolve().parents[1] / "artifacts"
SCREENSHOTS = ARTIFACTS / "screenshots"
VIDEOS = ARTIFACTS / "videos"
TRACES = ARTIFACTS / "traces"
load_dotenv(ENV_PATH)


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
        browser = p.chromium.launch(headless=False, slow_mo=750)
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
