from playwright.sync_api import Page, expect


class LoginPage:
    URL = "https://opensource-demo.orangehrmlive.com/"

    def __init__(self, page: Page):
        self.page = page

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

    # ---------- Actions ----------
    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    # ---------- Assertions ----------
    def assert_login_error(self):
        expect(self.error_message).to_be_visible()
