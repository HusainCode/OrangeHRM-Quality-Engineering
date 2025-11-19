"""
Centralized pytest fixtures for the test framework.
Provides browser, page, authentication, and page object fixtures.
"""
import pytest
from playwright.sync_api import Page, Browser, BrowserContext
from typing import Generator

from config import config
from pages import LoginPage, DashboardPage, PimPage, AdminPage, LeavePage, TimePage, MyInfoPage
from utils import data


# ============================================================================
# Browser and Page Fixtures
# ============================================================================

@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Browser launch arguments"""
    return {
        "headless": config.HEADLESS,
        "slow_mo": config.SLOW_MO,
    }


@pytest.fixture(scope="session")
def browser_context_args():
    """Browser context arguments"""
    return {
        "viewport": {"width": 1920, "height": 1080},
        "record_video_dir": config.VIDEOS_DIR if config.VIDEO_ON_FAILURE else None,
        "record_video_size": {"width": 1920, "height": 1080} if config.VIDEO_ON_FAILURE else None,
    }


@pytest.fixture(scope="function")
def context(browser: Browser, browser_context_args) -> Generator[BrowserContext, None, None]:
    """Create a new browser context for each test"""
    context = browser.new_context(**browser_context_args)

    # Enable tracing if configured
    if config.TRACE_ON_FAILURE:
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context

    # Stop tracing on test completion
    if config.TRACE_ON_FAILURE:
        context.tracing.stop(path=f"{config.TRACES_DIR}/trace.zip")

    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Generator[Page, None, None]:
    """Create a new page for each test"""
    page = context.new_page()

    # Set default timeouts from config
    page.set_default_timeout(config.DEFAULT_TIMEOUT)
    page.set_default_navigation_timeout(config.NAVIGATION_TIMEOUT)

    yield page

    page.close()


# ============================================================================
# Authentication Fixtures
# ============================================================================

@pytest.fixture(scope="function")
def authenticated_page(page: Page) -> Page:
    """
    Provide an authenticated page (logged in as admin).
    Use this fixture when tests require authentication.
    """
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(config.get_username(), config.get_password())

    # Wait for dashboard to confirm login success
    from playwright.sync_api import expect
    import re
    expect(page).to_have_url(re.compile("/dashboard"), timeout=15000)

    return page


# ============================================================================
# Page Object Fixtures
# ============================================================================

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Provide LoginPage instance"""
    return LoginPage(page)


@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    """Provide DashboardPage instance"""
    return DashboardPage(page)


@pytest.fixture
def pim_page(page: Page) -> PimPage:
    """Provide PimPage instance"""
    return PimPage(page)


@pytest.fixture
def admin_page(page: Page) -> AdminPage:
    """Provide AdminPage instance"""
    return AdminPage(page)


@pytest.fixture
def leave_page(page: Page) -> LeavePage:
    """Provide LeavePage instance"""
    return LeavePage(page)


@pytest.fixture
def time_page(page: Page) -> TimePage:
    """Provide TimePage instance"""
    return TimePage(page)


@pytest.fixture
def myinfo_page(page: Page) -> MyInfoPage:
    """Provide MyInfoPage instance"""
    return MyInfoPage(page)


# ============================================================================
# Authenticated Page Object Fixtures
# ============================================================================

@pytest.fixture
def authenticated_pim_page(authenticated_page: Page) -> PimPage:
    """Provide authenticated PimPage instance"""
    return PimPage(authenticated_page)


@pytest.fixture
def authenticated_admin_page(authenticated_page: Page) -> AdminPage:
    """Provide authenticated AdminPage instance"""
    return AdminPage(authenticated_page)


@pytest.fixture
def authenticated_leave_page(authenticated_page: Page) -> LeavePage:
    """Provide authenticated LeavePage instance"""
    return LeavePage(authenticated_page)


@pytest.fixture
def authenticated_time_page(authenticated_page: Page) -> TimePage:
    """Provide authenticated TimePage instance"""
    return TimePage(authenticated_page)


@pytest.fixture
def authenticated_myinfo_page(authenticated_page: Page) -> MyInfoPage:
    """Provide authenticated MyInfoPage instance"""
    return MyInfoPage(authenticated_page)


@pytest.fixture
def authenticated_dashboard_page(authenticated_page: Page) -> DashboardPage:
    """Provide authenticated DashboardPage instance"""
    return DashboardPage(authenticated_page)


# ============================================================================
# Test Data Fixtures
# ============================================================================

@pytest.fixture
def random_employee_data() -> dict:
    """Generate random employee data for tests"""
    first_name, last_name = data.random_full_name()
    return {
        "first_name": first_name,
        "last_name": last_name,
        "middle_name": data.random_string(6),
        "employee_id": data.random_employee_id(),
        "full_name": f"{first_name} {last_name}",
    }


@pytest.fixture
def random_user_data() -> dict:
    """Generate random user data for admin tests"""
    return {
        "username": data.random_username("testuser"),
        "password": data.random_password(12),
        "role": "ESS",
        "status": "Enabled",
    }


@pytest.fixture
def random_leave_data() -> dict:
    """Generate random leave data for leave tests"""
    from_date, to_date = data.random_date_range(1, 3)
    return {
        "leave_type": "CAN - Vacation",
        "from_date": from_date,
        "to_date": to_date,
        "comments": f"Test leave request {data.unique_timestamp()}",
    }


# ============================================================================
# Hooks for Screenshots and Artifacts
# ============================================================================

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshots on test failure"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Get the page fixture if it exists
        if "page" in item.funcargs or "authenticated_page" in item.funcargs:
            page = item.funcargs.get("page") or item.funcargs.get("authenticated_page")

            if config.SCREENSHOT_ON_FAILURE:
                try:
                    screenshot_path = f"{config.SCREENSHOTS_DIR}/{item.name}.png"
                    page.screenshot(path=screenshot_path)
                    print(f"\nScreenshot saved: {screenshot_path}")
                except Exception as e:
                    print(f"\nFailed to capture screenshot: {e}")
