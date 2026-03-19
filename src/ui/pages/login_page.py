from playwright.sync_api import Page, expect
from core.utils.user import User

class LoginPage:
    EMPTY_LOGIN_ERR = "Epic sadface: Username is required"
    INVALID_CREDENTIALS_ERR = "Epic sadface: Username and password do not match any user in this service"
    LOCKED_USER_ERR = "Epic sadface: Sorry, this user has been locked out."

    def __init__(self, page:Page, BASE_URL):
        self.page = page
        self.url = BASE_URL
        self.login_form = page.locator("div#login_button_container")
        self.error = page.locator("[data-test='error']")
        self.username_field = page.locator("input#user-name")
        self.password_field = page.locator("input#password")
        self.submit_button = page.locator("input#login-button")

    def open_page(self):
        self.page.goto(self.url)

    def assert_loaded(self):
        expect(self.login_form).to_be_visible()

    def assert_error(self, mssg: str):
        expect(self.error).to_be_visible()  
        expect(self.error).to_have_text(mssg)

    def empty_login(self):
        self.username_field.fill("")
        self.password_field.fill("")
        self.submit_button.click()
        self.assert_error(self.EMPTY_LOGIN_ERR)

    def invalid_username(self, PASSWORD):
        self.username_field.fill("something")
        self.password_field.fill(PASSWORD)
        self.submit_button.click()
        self.assert_error(self.INVALID_CREDENTIALS_ERR)

    def invalid_password(self, USERNAME):
        self.username_field.fill(USERNAME)
        self.password_field.fill("PASSWORD")
        self.submit_button.click()
        self.assert_error(self.INVALID_CREDENTIALS_ERR)

    def locked_out_user(self, user: User):
        self.username_field.fill(user.username)
        self.password_field.fill(user.password)
        self.submit_button.click()
        self.assert_error(self.LOCKED_USER_ERR)

    def valid_login(self, user: User):
        self.username_field.fill(user.username)
        self.password_field.fill(user.password)
        self.submit_button.click()
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def directly_open_inventory_page(self):
        self.page.goto("https://www.saucedemo.com/inventory.html")
        self.assert_loaded()

        