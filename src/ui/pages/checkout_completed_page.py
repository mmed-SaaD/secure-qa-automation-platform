from playwright.sync_api import Page, expect

class CheckoutCompletedPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_completed = page.get_by_role("heading", name="Thank you for your order!")
        self.back_to_home_button = page.locator("button#back-to-products")

    def assert_checkout_completed(self):
        expect(self.checkout_completed).to_be_visible()

    def back_to_home(self):
        self.back_to_home_button.click()

    
