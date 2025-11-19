"""
Navigation Tests - User navigation and logout
Tests for navigation flows and logout functionality.
"""
import pytest
from playwright.sync_api import Page
from pages import LoginPage, DashboardPage
from config import config
from utils import assertions


@pytest.mark.smoke
@pytest.mark.auth
class TestNavigation:
    """Navigation test suite"""

    def test_logout_returns_to_login_page(self, page: Page):
        """
        Test ID: NAV-LOGOUT-001
        Verify that logout returns user to login page
        """
        # Login first
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login(config.get_username(), config.get_password())

        # Verify on dashboard
        dashboard = DashboardPage(page)
        assertions.assert_on_dashboard(page)

        # Logout
        dashboard.logout()

        # Verify back on login page
        assertions.assert_on_login_page(page)
        assertions.assert_element_visible(login_page.login_button)
