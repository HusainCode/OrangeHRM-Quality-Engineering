"""
Base Page class that all page objects inherit from.
Contains common locators and actions shared across all pages.
"""
from playwright.sync_api import Page
from config import config


class BasePage:
    """Base class for all page objects"""

    def __init__(self, page: Page):
        self.page = page
        self.base_url = config.get_base_url()

    # Common locators across all pages
    @property
    def user_dropdown(self):
        """User dropdown in header"""
        return self.page.locator(".oxd-userdropdown-tab")

    @property
    def logout_link(self):
        """Logout link in user dropdown"""
        return self.page.get_by_role("menuitem", name="Logout")

    @property
    def success_toast(self):
        """Success toast notification"""
        return self.page.locator('.oxd-toast--success')

    @property
    def error_toast(self):
        """Error toast notification"""
        return self.page.locator('.oxd-toast--error')

    @property
    def info_toast(self):
        """Info toast notification"""
        return self.page.locator('.oxd-toast--info')

    @property
    def loading_spinner(self):
        """Loading spinner"""
        return self.page.locator('.oxd-loading-spinner')

    # Common actions
    def navigate_to(self, path: str = ""):
        """Navigate to a specific path"""
        url = f"{self.base_url}/{path}" if path else self.base_url
        self.page.goto(url)

    def logout(self):
        """Logout from application"""
        self.user_dropdown.click()
        self.logout_link.click()

    def wait_for_page_load(self, state: str = "domcontentloaded"):
        """Wait for page to load"""
        self.page.wait_for_load_state(state)

    def wait_for_network_idle(self):
        """Wait for network to be idle"""
        self.page.wait_for_load_state("networkidle")

    def get_success_toast_text(self) -> str:
        """Get success toast message text"""
        return self.success_toast.text_content()

    def get_error_toast_text(self) -> str:
        """Get error toast message text"""
        return self.error_toast.text_content()

    def click_menu_item(self, menu_name: str):
        """Click a main menu item by name"""
        self.page.get_by_role("link", name=menu_name).click()
