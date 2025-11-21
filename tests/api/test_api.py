"""
API Tests - Backend API testing
Tests for OrangeHRM API endpoints using Playwright's request context.
"""
import pytest
from playwright.sync_api import Page, APIRequestContext
from config import config


@pytest.mark.api
class TestAPI:
    """API test suite using Playwright request context"""

    @pytest.fixture
    def api_context(self, playwright) -> APIRequestContext:
        """Create API request context"""
        return playwright.request.new_context(
            base_url=config.get_base_url(),
            extra_http_headers={
                "Content-Type": "application/json",
            }
        )

    def test_api_login_returns_200(self, page: Page):
        """
        Test ID: API-AUTH-001
        Verify that login API returns successful status code (200 or 302 redirect)
        """
        # Navigate to login page to capture network requests
        page.goto(f"{config.get_base_url()}/web/index.php/auth/login")

        # Listen for API call
        with page.expect_response(lambda response: "/auth/" in response.url) as response_info:
            # Trigger login via UI
            page.locator('input[name="username"]').fill(config.get_username())
            page.locator('input[name="password"]').fill(config.get_password())
            page.get_by_role("button", name="Login").click()

        response = response_info.value

        # Assert status code is successful (200 OK or 302 redirect is acceptable)
        assert response.status in [200, 302], f"Expected 200/302, got {response.status}"

    def test_api_unauthorized_request_returns_401_or_redirect(self, api_context: APIRequestContext):
        """
        Test ID: API-AUTH-002
        Verify that unauthorized API request returns 401 or redirects
        """
        # Try to access protected endpoint without auth
        response = api_context.get("/web/index.php/api/v2/pim/employees")

        # Should return 401 Unauthorized or 302 Redirect to login
        assert response.status in [401, 302, 403], \
            f"Expected 401/302/403 for unauthorized request, got {response.status}"

    def test_api_response_time_acceptable(self, page: Page):
        """
        Test ID: API-PERF-001
        Verify that API responses are within acceptable time limits
        """
        import time

        page.goto(f"{config.get_base_url()}/web/index.php/auth/login")

        # Measure API response time
        start_time = time.time()

        with page.expect_response(lambda r: "/auth/" in r.url):
            page.locator('input[name="username"]').fill(config.get_username())
            page.locator('input[name="password"]').fill(config.get_password())
            page.get_by_role("button", name="Login").click()

        end_time = time.time()
        response_time = (end_time - start_time) * 1000

        # Assert response within 2 seconds
        assert response_time < 2000, f"API response time {response_time}ms exceeds 2000ms"
