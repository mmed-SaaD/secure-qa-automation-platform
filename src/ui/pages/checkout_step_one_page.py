from playwright.sync_api import Page, expect

class CheckoutStepOnePage:
    EMPTY_FORM_OR_EMPTY_FIRSTNAME = "Error: First Name is required"
    EMPTY_LASTNAME = "Error: Last Name is required"
    EMPTY_ZIP = "Error: Postal Code is required"

    def __init__(self, page: Page):
        self.page = page
        self.checkout_info_container = page.locator("div#checkout_info_container")
        self.first_name_field = page.locator("input#first-name")
        self.last_name_field = page.locator("input#last-name")
        self.zip_field = page.locator("input#postal-code")
        self.continue_button = page.get_by_role("button", name="Continue")
        self.form_error = page.locator('[data-test="error"]')

    def assert_loaded(self):
        expect(self.checkout_info_container).to_be_visible()

    def submit_empty_form(self):
        self.first_name_field.fill("")
        self.last_name_field.fill("")
        self.zip_field.fill("")
        self.continue_button.click()
        expect(self.form_error).to_be_visible()
        expect(self.form_error).to_have_text(self.EMPTY_FORM_OR_EMPTY_FIRSTNAME)

    def submit_form_with_missing_firstname(self, LASTNAME: str, ZIP: int):
        self.first_name_field.fill("")
        self.last_name_field.fill(LASTNAME)
        self.zip_field.fill(str(ZIP))
        self.continue_button.click()
        expect(self.form_error).to_be_visible()
        expect(self.form_error).to_have_text(self.EMPTY_FORM_OR_EMPTY_FIRSTNAME)

    def submit_form_with_missing_lastname(self, FIRSTNAME: str, ZIP: int):
        self.first_name_field.fill(FIRSTNAME)
        self.last_name_field.fill("")
        self.zip_field.fill(str(ZIP))
        self.continue_button.click()
        expect(self.form_error).to_be_visible()
        expect(self.form_error).to_have_text(self.EMPTY_LASTNAME)

    def submit_form_with_missing_zip(self, FIRSTNAME: str, LASTNAME: str):
        self.first_name_field.fill(FIRSTNAME)
        self.last_name_field.fill(LASTNAME)
        self.zip_field.fill("")
        self.continue_button.click()
        expect(self.form_error).to_be_visible()
        expect(self.form_error).to_have_text(self.EMPTY_ZIP)

    def submit_form_with_required_fields(self, FIRSTNAME: str, LASTNAME: str, ZIP: int):
        self.first_name_field.fill(FIRSTNAME)
        self.last_name_field.fill(LASTNAME)
        self.zip_field.fill(str(ZIP))
        self.continue_button.click()
        
