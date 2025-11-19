import pytest
import re
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


# ---------------------------
# NAV-LOGOUT-001: Logout returns to login
# ---------------------------
def test_logout_returns_to_login(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    # login first
    login.navigate()
    login.login("Admin", "admin123")
    dashboard.assert_on_dashboard()

    # logout
    dashboard.logout()

    # verify back on login page
    expect(page).to_have_url(re.compile("/auth/login"))
    login.assert_page_loaded()
