import pytest
from src.ui.pages.login_page import LoginPage 
from src.ui.pages.inventory_page import InventoryPage 
from core.utils.user import User


@pytest.mark.ui 
@pytest.mark.smoke 
def test_ui_login_items_checked(page, BASE_URL, USERNAME, PASSWORD):
    login_page = LoginPage(page, BASE_URL) 
    standard_user = User(USERNAME, PASSWORD)
    login_page.open_page() 
    login_page.assert_loaded() 
    login_page.valid_login(standard_user)
    inventory_page = InventoryPage(page) 
    inventory_page.assert_list_is_loaded()
    inventory_page.view_and_assert_details()

'''
@pytest.mark.ui 
@pytest.mark.smoke 
def test_ui_sort_items_adsc():
'''