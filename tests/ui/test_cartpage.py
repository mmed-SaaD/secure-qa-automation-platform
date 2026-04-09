import pytest
from src.ui.pages.cart_page import CartPage 

@pytest.mark.ui
@pytest.mark.smoke
def test_ui_login_check_cart_count_matches(page, login_to_inventory_page, cart_page_with_items):
    cart_label = login_to_inventory_page.get_cart_count()
    login_to_inventory_page.go_to_cart()
    cart_page_with_items.assert_cart_count_update(cart_label)
