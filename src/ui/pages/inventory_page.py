from playwright.sync_api import Page, expect
from typing import Tuple
from core.utils.extract_id import extract_id
from core.utils.assert_sort import assert_sort
import random, re

class InventoryPage:
    def __init__(self, page:Page):
        self.page = page
        ############################# Sidebar menu #########################################
        self.burger_menu = page.locator("button#react-burger-menu-btn")
        self.menu_about_option = page.locator('[data-test="about-sidebar-link"]')
        self.menu_reset_app_option = page.locator('[data-test="reset-sidebar-link"]')
        ############################ App ##################################################
        self.inv_container = page.locator("[data-test='inventory-container']")
        self.inv_details_container = page.locator("#inventory_item_container")
        self.inv_details_button = self.inv_details_container.locator("button")
        self.inv_items = self.page.locator(".inventory_item")
        self.back_to_products_button = page.get_by_role("button", name="Back to products")
        self.cart_button = page.locator("[data-test='shopping-cart-link']")
        ########################## Footer #################################################
        self.twitter = page.locator('[data-test="social-twitter"]')
        self.facebook = page.locator('[data-test="social-facebook"]')
        self.linkedin = page.locator('[data-test="social-linkedin"]')

    def assert_list_is_loaded(self):
        expect(self.inv_container).to_be_visible()

    def get_details(self, item_id: int) -> Tuple[str, str]:
        expect(self.page).to_have_url(re.compile(rf"inventory-item\.html\?id={item_id}"))
        details_container = self.page.locator("[data-test='inventory-item']")
        details_title = details_container.locator("[data-test='inventory-item-name']").inner_text()
        details_price = details_container.locator("[data-test='inventory-item-price']").inner_text()
        return details_title, details_price

    def get_items_count(self) -> int:
        items_count = self.inv_items.count()
        if items_count == 0:
            raise ValueError("No items were found in the list")
        return items_count

    def get_items_titles(self) -> list[str]:
        items_titles = []
        items_count = self.get_items_count()
        for item in range (0, items_count):
            title = self.inv_items.nth(item).locator("[data-test='inventory-item-name']").inner_text()
            items_titles.append(title)
        return items_titles

    def get_items_prices(self) -> list[float]:
        items_prices = []
        items_count = self.get_items_count()
        for item in range (0, items_count):
            price = self.inv_items.nth(item).locator("[data-test='inventory-item-price']").inner_text()
            price = float(price.replace("$","").strip())
            items_prices.append(price)
        return items_prices

    def select_random_item(self) -> int:
        items_count = self.get_items_count()
        rand_item_id = random.randint(0, items_count-1)
        return rand_item_id

    def assert_details(self, item_id:int,  title: str, price: str):
        details_title, details_price = self.get_details(item_id)
        assert title == details_title, f"Expected title '{title}', got '{details_title}'"
        assert price == details_price, f"Expected price '{price}', got '{details_price}'"

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

    def sort_items(self, option: str | None = None):
        if option is None:
            self.page.select_option("[data-test='product-sort-container']", value="za")
            items_titles = self.get_items_titles()
            assert_sort(items_titles, None, True)
            self.page.select_option("[data-test='product-sort-container']", value="az")
            items_titles = self.get_items_titles()
            assert_sort(items_titles, None)
            self.page.select_option("[data-test='product-sort-container']", value="lohi")
            items_prices = self.get_items_prices()
            assert_sort(items_prices,float)
            self.page.select_option("[data-test='product-sort-container']", value="hilo")
            items_prices = self.get_items_prices()
            assert_sort(items_prices,float, True)
            
        match option:
            case "za":
                self.page.select_option("[data-test='product-sort-container']", value="za")
                items_titles = self.get_items_titles()
                assert_sort(items_titles, None, True)
            case "az":
                self.page.select_option("[data-test='product-sort-container']", value="az")
                items_titles = self.get_items_titles()
                assert_sort(items_titles, None)
            case "lohi":
                self.page.select_option("[data-test='product-sort-container']", value="lohi")
                items_prices = self.get_items_prices()
                assert_sort(items_prices,float)
            case "hilo":
                self.page.select_option("[data-test='product-sort-container']", value="hilo")
                items_prices = self.get_items_prices()
                assert_sort(items_prices,float, True)

    def add_to_cart_from_list(self, index: int | None = None):
        if index is None:
            index = self.select_random_item()
        inv_item_container = self.page.locator(".inventory_item").nth(index)
        item_add_to_cart_button = inv_item_container.locator("button")
        if item_add_to_cart_button.inner_text() == "Add to cart":
            item_add_to_cart_button.click()
        else:
            pass

    def add_to_cart_from_details(self, index: int | None = None):
        self.view_and_assert_details(index)
        if self.inv_details_button.inner_text() == "Add to cart":
            self.inv_details_button.click()
            self.back_to_products()
        else:
            self.back_to_products()
            pass

    def remove_item_from_list(self, index: int):
        inv_item_container = self.page.locator(".inventory_item").nth(index)
        inv_item_container.get_by_role("button", name="Remove").click()

    def remove_from_details(self, index: int):
        self.view_and_assert_details(index)
        self.inv_details_container.locator('button').click()
        self.back_to_products()

    def go_to_cart(self):
        self.cart_button.click()

    def get_cart_count(self) -> int:
        cart_count = self.page.locator("[data-test='shopping-cart-badge']")
        try:
            expect(cart_count).to_be_visible()
            return int(cart_count.inner_text())
        except:
            return 0

    def back_to_products(self):
        self.back_to_products_button.click() 
        self.assert_list_is_loaded()

    def refresh_page(self):
        self.page.reload()

    def assert_cart_count_persistance(self):
        cart_count_before_refresh = self.get_cart_count()
        self.refresh_page()
        assert int(cart_count_before_refresh) == int(self.get_cart_count()) , \
        f"cart count expected to remain the same, was {cart_count_before_refresh} became {self.get_cart_count()}"

    def visit_twitter(self):
        with self.page.expect_popup() as popup_info:
            self.twitter.click()
            new_tab = popup_info.value
            new_tab.wait_for_load_state("networkidle")
            url = new_tab.url
            assert "x.com/saucelabs" in url or "twitter.com/saucelabs" in url, \
            f"There is a url missmatch, expecting https://x.com/saucelabs but recieved {url}"

    def visit_facebook(self):
        with self.page.expect_popup() as popup_info:
            self.facebook.click()
            new_tab = popup_info.value
            new_tab.wait_for_load_state("networkidle")
            url = new_tab.url
            assert url == "https://web.facebook.com/saucelabs?_rdc=1&_rdr", \
            f"There is a url missmatch, expecting https://web.facebook.com/saucelabs?_rdc=1&_rdr but recieved {url}"

    def visit_linkedin(self):
        with self.page.expect_popup() as popup_info:
            self.linkedin.click()
            new_tab = popup_info.value
            new_tab.wait_for_load_state("networkidle")
            url = new_tab.url
            assert url == "https://www.linkedin.com/company/sauce-labs/", \
            f"There is a url missmatch, expecting https://www.linkedin.com/company/sauce-labs/ but recieved {url}"

    def visit_about(self):
        self.burger_menu.click()
        self.menu_about_option.click()
        assert self.page.url == "https://saucelabs.com/", \
        f"There is a url missmatch, expecting https://saucelabs.com/ but recieved {self.page.url}"
    
    def reset_app_state(self):
        self.burger_menu.click()
        self.menu_reset_app_option.click()
        assert self.get_cart_count() == 0, \
        f"Cart count is still the same even after resetting the app"

    def logout(self):
        self.burger_menu.click()
        self.page.get_by_role("link", name="Logout").click()
        expect(self.page).to_have_url("https://www.saucedemo.com/")

