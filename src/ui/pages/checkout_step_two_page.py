from playwright.sync_api import Page, expect
import re

class CheckoutStepTwoPage:
    def __init__(self, page: Page):
        self.page = page
        self.overview_header = page.locator('[data-test="secondary-header"]')
        self.checkout_items = page.locator('[data-test="inventory-item"]')
        self.checkout_total_price = page.locator('[data-test="total-label"]')
        self.checkout_tax = page.locator('[data-test="tax-label"]')
        self.payment_info = page.locator('[data-test="payment-info-value"]')
        self.finish_button = page.get_by_role("button", name="Finish")

    def assert_loaded(self):
        expect(self.overview_header).to_be_visible()

    def assert_payment_info(self, payment_info: str):
        assert str(self.payment_info.inner_text()) == str(payment_info)

    def assert_total_price(self):
        items_prices = []
        for index in range(0, self.checkout_items.count()):
            price = self.checkout_items.nth(index).locator('[data-test="inventory-item-price"]').inner_text()
            price = float(re.search(r'\d+\.\d+', price).group())
            items_prices.append(price)
        
        checkout_total = float(re.search(r'\d+\.\d+', self.checkout_total_price.inner_text()).group()) 
        tax = float(re.search(r'\d+\.\d+', self.checkout_tax.inner_text()).group()) 
        assert round(sum(items_prices) + tax, 2) == round(checkout_total, 2), \
        f"Total calculated is : {sum(items_prices) + tax} while the total fetched from the checkout is : {checkout_total}"

    def finish_checkout(self):
        self.finish_button.click()
        
