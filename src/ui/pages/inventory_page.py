from playwright.sync_api import Page, expect
from typing import Tuple
from core.utils.extract_id import extract_id
import random

class InventoryPage:
    def __init__(self, page:Page):
        self.page = page
        self.burger_menu = page.locator("button#react-burger-menu-btn")
        self.inv_container = page.locator("[data-test='inventory-container']")
        self.inv_details_container = page.locator("#inventory_item_container")
        self.inv_items = self.page.locator(".inventory_item")
        self.back_to_products_button = page.get_by_role("button", name="Back to products")

    def assert_list_is_loaded(self):
        expect(self.inv_container).to_be_visible()

    def get_details(self, item_id: int) -> Tuple[str, str]:
        expect(self.page).to_have_url(lambda url: f"inventory-item.html?id={item_id}" in url)
        details_container = self.page.locator("[data-test='inventory-item']")
        details_title = details_container.locator("[data-test='inventory-item-name']").inner_text()
        details_price = details_container.locator("[data-test='inventory-item-price']").inner_text()
        return details_title, details_price

    def get_items_count(self) -> int:
        items_count = self.inv_items.count()
        if items_count == 0:
            raise ValueError("No items were found in the list")
        return items_count

    def select_random_item(self) -> int:
        items_count = self.get_items_count()
        rand_item_id = random.randint(0, items_count-1)
        return rand_item_id

    def assert_details(self, item_id:int,  title: str, price: str):
        details_title, details_price = self.get_details(item_id)
        assert title == details_title
        assert price == details_price

    def view_and_assert_details(self, index:int | None = None):   
        if index is None:
            index = self.select_random_item()
        inv_item_container = self.page.locator(".inventory_item").nth(index)
        title = inv_item_container.locator("[data-test='inventory-item-name']").inner_text()
        price = inv_item_container.locator("[data-test='inventory-item-price']").inner_text()
        item_link = inv_item_container.locator("div.inventory_item_img > a")
        id_attr_value = item_link.get_attribute("id")
        if id_attr_value is None:
            raise ValueError("Item link id attribute is missing")
        item_id = extract_id(id_attr_value)
        item_link.click()
        self.inv_details_container.wait_for(state="visible")
        self.assert_details(item_id, title, price)
        self.back_to_products_button.click() 
        self.assert_list_is_loaded()
        
    def logout(self):
        self.burger_menu.click()
        self.page.get_by_role("link", name="Logout").click()
        expect(self.page).to_have_url("https://www.saucedemo.com/")

