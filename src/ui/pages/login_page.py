from playwright.sync_api import Page, expect
from core.utils.user import User

class LoginPage:
    EMPTY_LOGIN_ERR = "Epic sadface: Username is required"
    INVALID_CREDENTIALS_ERR = "Epic sadface: Username and password do not match any user in this service"
    LOCKED_USER_ERR = "Epic sadface: Sorry, this user has been locked out."

    def __init__(self, page:Page, base_url: str):
        self.page = page
        self.url = base_url
        self.login_form = page.locator("div#login_button_container")
        self.error = page.locator("[data-test='error']")

    def open_page(self):
        self.page.goto(self.url)

    def assert_loaded(self):
        expect(self.login_form).to_be_visible()

    def assert_error(self, mssg: str):
        expect(self.error).to_be_visible()  
        expect(self.error).to_have_text(mssg)

    def empty_login(self):
        self.page.locator("input#user-name").fill("")
        self.page.locator("input#password").fill("")
        self.page.locator("input#login-button").click()
        self.assert_error(self.EMPTY_LOGIN_ERR)

    def invalid_username(self, PASSWORD):
        self.page.locator("input#user-name").fill("something")
        self.page.locator("input#password").fill(PASSWORD)
        self.page.locator("input#login-button").click()
        self.assert_error(self.INVALID_CREDENTIALS_ERR)

    def invalid_password(self, USERNAME):
        self.page.locator("input#user-name").fill(USERNAME)
        self.page.locator("input#password").fill("PASSWORD")
        self.page.locator("input#login-button").click()
        self.assert_error(self.INVALID_CREDENTIALS_ERR)

    def locked_out_user(self, user: User):
        self.page.locator("input#user-name").fill(user.username)
        self.page.locator("input#password").fill(user.password)
        self.page.locator("input#login-button").click()
        self.assert_error(self.LOCKED_USER_ERR)

    def valid_login(self, user: User):
        self.page.locator("input#user-name").fill(user.username)
        self.page.locator("input#password").fill(user.password)
        self.page.locator("input#login-button").click()
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")

        