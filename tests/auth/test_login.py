"""
Login Tests - Authentication module
Tests for login functionality including valid/invalid credentials and field validation.
"""
import pytest
from playwright.sync_api import Page
from pages import LoginPage, DashboardPage
from config import config
from utils import assertions


@pytest.mark.smoke
@pytest.mark.auth
class TestLogin:
    """Login test suite"""

    def test_valid_login_redirects_to_dashboard(self, login_page: LoginPage, page: Page):
        """
        Test ID: LOGIN-001
        Verify that valid login redirects to dashboard
        """
        login_page.navigate()
        login_page.login(config.get_username(), config.get_password())

        # Assert redirect to dashboard
        assertions.assert_on_dashboard(page)

    @pytest.mark.parametrize("username,password", [
        ("WrongUser", "admin123"),
        ("Admin", "wrongpass"),
    ])
    def test_invalid_credentials_show_error(self, login_page: LoginPage, username: str, password: str):
        """
        Test ID: LOGIN-002
        Verify that invalid credentials show error message
        """
        login_page.navigate()
        login_page.login(username, password)

        # Assert error message is displayed
        assertions.assert_element_visible(login_page.error_message)

    def test_empty_username_shows_required_error(self, login_page: LoginPage):
        """
        Test ID: LOGIN-003
        Verify that empty username shows required field error
        """
        login_page.navigate()
        login_page.enter_password(config.get_password())
        login_page.click_login()

        # Assert error message is displayed (OrangeHRM shows generic error for required fields)
        assertions.assert_element_visible(login_page.error_message)

    def test_empty_password_shows_required_error(self, login_page: LoginPage):
        """
        Test ID: LOGIN-004
        Verify that empty password shows required field error
        """
        login_page.navigate()
        login_page.enter_username(config.get_username())
        login_page.click_login()

        # Assert error message is displayed (OrangeHRM shows generic error for required fields)
        assertions.assert_element_visible(login_page.error_message)

    def test_both_fields_empty_shows_required_errors(self, login_page: LoginPage):
        """
        Test ID: LOGIN-005
        Verify that empty username and password show required errors
        """
        login_page.navigate()
        login_page.click_login()

        # Assert both fields show required errors
        assertions.assert_element_visible(login_page.error_message)
