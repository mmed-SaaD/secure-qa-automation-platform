import pytest
import pytz

from datetime import datetime

from src.ui.pages.checkout_step_one_page import CheckoutStepOnePage
from src.ui.pages.checkout_step_two_page import CheckoutStepTwoPage
from src.ui.pages.checkout_completed_page import CheckoutCompletedPage
from core.utils.performance_helpers import action_time_spent, append_performance_results_to_report


@pytest.mark.performance_ui
@pytest.mark.parametrize("iteration", range(1, 6))
def test_ui_checkout_happy_path_performance(
    iteration,
    login_to_inventory_page,
    cart_page_with_items,
    proceed_to_checkout,
    page,
    FIRSTNAME,
    LASTNAME,
    ZIP,
    PAYMENT_INFO,
):
    test_name = "checkout_happy_path"

    checkout_step_one_page = CheckoutStepOnePage(page)
    checkout_step_two_page = CheckoutStepTwoPage(page)
    checkout_completed_page = CheckoutCompletedPage(page)

    checkout_step_one_page.assert_loaded()

    duration_step_1 = action_time_spent(
        lambda: (
            checkout_step_one_page.submit_form_with_required_fields(FIRSTNAME, LASTNAME, ZIP),
            page.wait_for_url("**/checkout-step-two.html"),
        )
    )

    checkout_step_two_page.assert_loaded()
    checkout_step_two_page.assert_payment_info(PAYMENT_INFO)
    checkout_step_two_page.assert_total_price()

    append_performance_results_to_report(test_name, iteration, "checkout_info_to_overview", duration_step_1, datetime.now(tz=pytz.timezone('Africa/Casablanca')).strftime("%Y-%m-%d %H:%M:%S"))

    duration_step_2 = action_time_spent(
        lambda: (
            checkout_step_two_page.finish_checkout(),
            page.wait_for_url("**/checkout-complete.html"),
        )
    )

    checkout_completed_page.assert_checkout_completed()

    append_performance_results_to_report(test_name, iteration, "overview_to_complete", duration_step_2, datetime.now(tz=pytz.timezone('Africa/Casablanca')).strftime("%Y-%m-%d %H:%M:%S"))
