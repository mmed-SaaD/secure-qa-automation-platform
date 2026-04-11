import pytest
from src.ui.pages.login_page import LoginPage 
from src.ui.pages.cart_page import CartPage

@pytest.mark.ui 
@pytest.mark.smoke 
def test_ui_login_items_checked(login_to_inventory_page):
    inventory_page = login_to_inventory_page
    inventory_page.view_and_assert_details()

@pytest.mark.ui
@pytest.mark.smoke
def test_ui_login_sort_items(login_to_inventory_page):
    inventory_page = login_to_inventory_page
    inventory_page.sort_items()

@pytest.mark.ui
@pytest.mark.smoke
def test_ui_login_add_items_to_cart(page, login_to_inventory_page, cart_page_with_items):
    inventory_page = login_to_inventory_page
    cart_label = inventory_page.get_cart_count()
    inventory_page.go_to_cart()
    cart_page = CartPage(page)
    cart_page.assert_cart_count_update(cart_label)

    cart_page.remove_item_from_cart(2)

    inventory_page.remove_item_from_list(1)

    inventory_page.remove_from_details(3)
    
    inventory_page.add_to_cart_from_list(1)
    inventory_page.add_to_cart_from_details(3)


@pytest.mark.ui
@pytest.mark.smoke
def test_ui_login_refresh_page_check_cart_count_persists(login_to_inventory_page, page, cart_page_with_items):
    login_to_inventory_page.assert_cart_count_persistance()

@pytest.mark.ui
@pytest.mark.smoke
def test_ui_bypass_loginpage_to_inventorypage(BASE_URL, login_to_inventory_page, page):
    login_to_inventory_page.logout()
    login_page = LoginPage(page, BASE_URL)
    login_page.directly_open_inventory_page()

@pytest.mark.ui
@pytest.mark.smoke
def test_ui_new_tab(login_to_inventory_page, context, page, BASE_URL):
    new_page = context.new_page()
    new_page.goto(BASE_URL)
    login_page = LoginPage(new_page, BASE_URL)
    login_page.assert_loaded()

@pytest.mark.ui
@pytest.mark.smoke
def test_ui_new_session(login_to_inventory_page,browser, BASE_URL):
    new_context = browser.new_context()
    new_page = new_context.new_page()
    new_page.goto(BASE_URL)

    login_page = LoginPage(new_page, BASE_URL)
    login_page.assert_loaded()

    new_context.close()
