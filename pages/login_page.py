from playwright.sync_api import Page, expect


class LoginPage:
    URL = "https://opensource-demo.orangehrmlive.com/"

    def __init__(self, loginPage: Page):
        self.page = loginPage

    # ---------- Navigation ----------
    def navigate(self):
        self.page.goto(self.URL)

    # ---------- Locators ----------
    @property
    def username_input(self):
        return self.page.locator('input[name="username"]')

    @property
    def password_input(self):
        return self.page.locator('input[name="password"]')

    @property
    def login_button(self):
        return self.page.get_by_role("button", name="Login")

    @property
    def error_message(self):
        return self.page.locator(
            ".oxd-alert-content-text, .oxd-input-field-error-message"
        ).first

    @property
    def forgot_password_link(self):
        return self.page.get_by_text("Forgot your password?")

    @property
    def page_title(self):
        return self.page.locator(".oxd-text--h5")

    # ---------- Actions ----------
    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_text(self):
        return self.error_message.text_content()

    def click_forgot_password(self):
        self.forgot_password_link.click()

    def is_page_loaded(self):
        return self.page_title.is_visible() and self.login_button.is_visible()

    # ---------- Assertions ----------
    def assert_login_error(self):
        expect(self.error_message).to_be_visible()

    def assert_page_loaded(self):
        expect(self.page_title).to_be_visible()
        expect(self.login_button).to_be_visible()
