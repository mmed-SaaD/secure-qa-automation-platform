import os
import pytest
import re
from pathlib import Path
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright


ENV_PATH = Path(__file__).resolve().parents[1] / ".env"
ARTIFACTS = Path(__file__).resolve().parents[1] / "artifacts"
SCREENSHOTS = ARTIFACTS / "screenshots"
VIDEOS = ARTIFACTS / "videos"
TRACES = ARTIFACTS / "traces"
load_dotenv(ENV_PATH)

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
        raise ValueError("No password found in .venv")
    return password

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=750)
        yield browser
        browser.close()

@pytest.fixture(scope="session")
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

@pytest.fixture(scope="session")
def page(context, request):
    page = context.new_page()
    yield page

    #get request.node.rep_call and if it does not exist return None
    failed = getattr(request.node, "rep_call", None) and request.node.rep_call.failed
    print(f"failed : {failed}")

    safe_name = re.sub(r"[^a-zA-Z0-9_.-]+","_", request.node.nodeid)

    if failed:
        page.screenshot(path=str(SCREENSHOTS / f"/{safe_name}.png"))
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
