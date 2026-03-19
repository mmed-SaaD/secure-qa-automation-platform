import pytest
from src.ui.pages.checkout_step_one_page import CheckoutStepOnePage
from src.ui.pages.checkout_step_two_page import CheckoutStepTwoPage
from src.ui.pages.checkout_completed_page import CheckoutCompletedPage

'''
@pytest.mark.ui
def test_ui_login_checkout_empty_form(login_to_inventory_page, cart_page_with_items, page, proceed_to_checkout):
    checkout_step_one_page = CheckoutStepOnePage(page)
    checkout_step_one_page.submit_empty_form()

@pytest.mark.ui
def test_ui_login_checkout_empty_firstname(login_to_inventory_page, page, LASTNAME, ZIP, cart_page_with_items, proceed_to_checkout):
    checkout_step_one_page = CheckoutStepOnePage(page)
    checkout_step_one_page.submit_form_with_missing_firstname(LASTNAME, ZIP)

@pytest.mark.ui
def test_ui_login_checkout_empty_lastname(login_to_inventory_page, page, FIRSTNAME, ZIP, cart_page_with_items, proceed_to_checkout):
    checkout_step_one_page = CheckoutStepOnePage(page)
    checkout_step_one_page.submit_form_with_missing_lastname(FIRSTNAME, ZIP)

@pytest.mark.ui
def test_ui_login_checkout_empty_zip(login_to_inventory_page, page, FIRSTNAME, LASTNAME, cart_page_with_items, proceed_to_checkout):
    checkout_step_one_page = CheckoutStepOnePage(page)
    checkout_step_one_page.submit_form_with_missing_zip(FIRSTNAME, LASTNAME)

@pytest.mark.ui
@pytest.mark.smoke
def test_ui_login_add_items_to_cart_checkout(login_to_inventory_page, page, FIRSTNAME, LASTNAME, ZIP, PAYMENT_INFO, cart_page_with_items, proceed_to_checkout):
    checkout_step_one_page = CheckoutStepOnePage(page)
    checkout_step_one_page.submit_form_with_required_fields(FIRSTNAME, LASTNAME, ZIP)
    checkout_step_two_page = CheckoutStepTwoPage(page)
    checkout_step_two_page.assert_loaded()
    checkout_step_two_page.assert_payment_info(PAYMENT_INFO)
    checkout_step_two_page.assert_total_price()
    checkout_step_two_page.finish_checkout()
    checkout_completed_page = CheckoutCompletedPage(page)
    checkout_completed_page.assert_checkout_completed()
    checkout_completed_page.back_to_home()
'''