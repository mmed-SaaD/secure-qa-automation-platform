from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page:Page):
        self.page = page
        self.cart_list = page.locator('[data-test="cart-list"]')
        self.checkout_button = page.locator("button#checkout")
        self.continue_shopping_button =  page.locator("button#continue-shopping")
        self.cart_list_item = page.locator('[data-test="inventory-item"]')

    def assert_loaded(self):
        expect(self.cart_list).to_be_visible()

    def continue_shopping(self):
        self.continue_shopping_button.click()

    def checkout(self):
        self.checkout_button.click()

    def remove_item_from_cart(self, index):
        self.cart_list_item.nth(index).locator("button").click()
        self.continue_shopping()

    def assert_cart_count_update(self, cart_label_count: int):
        cart_list_count = int(self.page.locator('[data-test="inventory-item"]').count())
        #self.page.locator('[data-test="continue-shopping"]').click()
        assert cart_label_count == cart_list_count, \
        f"Cart badge shows {cart_label_count}, but cart contains {cart_list_count} items"