"""
Login Page Object - handles all login page interactions.
Follows clean POM pattern: locators + actions only, no assertions.
"""
from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Login page object for OrangeHRM"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.path = "web/index.php/auth/login"

    # ---------- Locators ----------
    @property
    def username_input(self):
        """Username input field"""
        return self.page.locator('input[name="username"]')

    @property
    def password_input(self):
        """Password input field"""
        return self.page.locator('input[name="password"]')

    @property
    def login_button(self):
        """Login button"""
        return self.page.get_by_role("button", name="Login")

    @property
    def error_message(self):
        """Error message displayed on login failure"""
        return self.page.locator(
            ".oxd-alert-content-text, .oxd-input-field-error-message"
        ).first

    @property
    def forgot_password_link(self):
        """Forgot password link"""
        return self.page.get_by_text("Forgot your password?")

    @property
    def page_title(self):
        """Login page title"""
        return self.page.locator(".oxd-text--h5")

    @property
    def username_required_error(self):
        """Username required error message"""
        return self.username_input.locator('..').locator('.oxd-input-field-error-message')

    @property
    def password_required_error(self):
        """Password required error message"""
        return self.password_input.locator('..').locator('.oxd-input-field-error-message')

    # ---------- Actions ----------
    def navigate(self):
        """Navigate to login page"""
        self.navigate_to(self.path)

    def enter_username(self, username: str):
        """Enter username"""
        self.username_input.fill(username)

    def enter_password(self, password: str):
        """Enter password"""
        self.password_input.fill(password)

    def click_login(self):
        """Click login button"""
        # Ensure button is visible and ready
        self.login_button.wait_for(state="visible", timeout=5000)
        self.login_button.click()
        self.wait_for_page_load()

    def login(self, username: str, password: str):
        """Perform complete login action"""
        self.enter_username(username)
        self.enter_password(password)
        # Small wait to ensure form is ready
        self.page.wait_for_timeout(200)
        self.click_login()

    def get_error_text(self) -> str:
        """Get error message text"""
        return self.error_message.text_content()

    def click_forgot_password(self):
        """Click forgot password link"""
        self.forgot_password_link.click()

    def is_page_loaded(self) -> bool:
        """Check if login page is fully loaded"""
        return self.page_title.is_visible() and self.login_button.is_visible()
