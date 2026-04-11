import pytest

@pytest.mark.ui
@pytest.mark.smoke
def test_ui_visit_twitter(login_to_inventory_page):
    login_to_inventory_page.visit_twitter()
'''
@pytest.mark.ui
@pytest.mark.smoke
def test_ui_visit_facebook(login_to_inventory_page):
    login_to_inventory_page.visit_facebook()

@pytest.mark.ui
@pytest.mark.smoke
def test_ui_visit_linkedin(login_to_inventory_page):
    login_to_inventory_page.visit_linkedin()

@pytest.mark.ui
@pytest.mark.smoke
def test_ui_visit_about(login_to_inventory_page):
    login_to_inventory_page.visit_about()

@pytest.mark.ui
@pytest.mark.smoke
def test_ui_resetting_app_state(login_to_inventory_page, cart_page_with_items):
    login_to_inventory_page.reset_app_state()
'''