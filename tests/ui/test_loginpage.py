import pytest
from src.ui.pages.login_page import LoginPage 
from src.ui.pages.inventory_page import InventoryPage 
from core.utils.user import User

@pytest.mark.ui 
@pytest.mark.smoke 
def test_ui_login_and_logout(page, BASE_URL, USERNAME, PASSWORD): 
    login_page = LoginPage(page, BASE_URL) 
    standard_user = User(USERNAME, PASSWORD)
    login_page.open_page() 
    login_page.assert_loaded() 
    login_page.valid_login(standard_user)
    inventory_page = InventoryPage(page) 
    inventory_page.logout()

@pytest.mark.ui
def test_ui_empty_login_shows_err(page, BASE_URL):
    login_page = LoginPage(page, BASE_URL)
    login_page.open_page() 
    login_page.assert_loaded() 
    login_page.empty_login() 

@pytest.mark.ui
def test_ui_invalid_username_shows_err(page, BASE_URL, PASSWORD):
    login_page = LoginPage(page, BASE_URL)
    login_page.open_page() 
    login_page.assert_loaded()
    login_page.invalid_username(PASSWORD) 

@pytest.mark.ui
def test_ui_invalid_password_shows_err(page, BASE_URL, USERNAME):
    login_page = LoginPage(page, BASE_URL)
    login_page.open_page() 
    login_page.assert_loaded()
    login_page.invalid_password(USERNAME) 

@pytest.mark.ui
def test_ui_locked_out_user_shows_err(page, BASE_URL, LOCKEDUSER, PASSWORD):
    login_page = LoginPage(page, BASE_URL)
    locked_user = User(LOCKEDUSER, PASSWORD)
    login_page.open_page() 
    login_page.assert_loaded()
    login_page.locked_out_user(locked_user)
