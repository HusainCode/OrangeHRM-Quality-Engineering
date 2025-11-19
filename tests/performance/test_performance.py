"""
Performance Tests - Page load and interaction performance
Basic performance checks using Playwright's timing API.
"""
import pytest
from playwright.sync_api import Page
from pages import LoginPage, PimPage, DashboardPage
from config import config
from utils import waits


@pytest.mark.performance
@pytest.mark.slow
class TestPerformance:
    """Performance test suite"""

    def test_login_page_load_time(self, page: Page):
        """
        Test ID: PERF-001
        Verify that login page loads within acceptable time
        """
        login_page = LoginPage(page)

        # Start timing
        page.goto(login_page.base_url)

        # Measure load time
        load_state = page.wait_for_load_state("domcontentloaded", timeout=5000)

        # Check performance navigation timing
        timing = page.evaluate("""() => {
            const perfData = window.performance.timing;
            return {
                loadTime: perfData.loadEventEnd - perfData.navigationStart,
                domContentLoaded: perfData.domContentLoadedEventEnd - perfData.navigationStart
            };
        }""")

        # Assert load time is reasonable (< 3 seconds)
        assert timing['loadTime'] < 3000, f"Page load time {timing['loadTime']}ms exceeds 3000ms threshold"

    def test_dashboard_page_load_time_after_login(self, page: Page):
        """
        Test ID: PERF-002
        Verify that dashboard loads quickly after login
        """
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login(config.get_username(), config.get_password())

        # Wait for dashboard
        waits.wait_for_url_change(page, "/dashboard")

        # Check timing
        timing = page.evaluate("""() => {
            return performance.now();
        }""")

        assert timing < 5000, f"Dashboard load time {timing}ms exceeds 5000ms threshold"

    def test_employee_search_response_time(self, authenticated_pim_page: PimPage):
        """
        Test ID: PERF-003
        Verify that employee search responds within acceptable time
        """
        pim = authenticated_pim_page

        pim.navigate()
        waits.wait_for_network_idle(pim.page)

        # Measure search time
        import time
        start_time = time.time()

        pim.search_employee_by_name("Peter")
        waits.wait_for_network_idle(pim.page)

        end_time = time.time()
        search_time = (end_time - start_time) * 1000  # Convert to milliseconds

        # Assert search completes within 3 seconds
        assert search_time < 3000, f"Search time {search_time}ms exceeds 3000ms threshold"

    def test_page_navigation_performance(self, authenticated_page: Page):
        """
        Test ID: PERF-004
        Verify navigation between major modules is performant
        """
        import time

        modules = ["PIM", "Admin", "Leave", "Time"]
        navigation_times = []

        for module in modules:
            start = time.time()

            # Click module link
            authenticated_page.get_by_role("link", name=module).click()
            authenticated_page.wait_for_load_state("domcontentloaded")

            end = time.time()
            nav_time = (end - start) * 1000
            navigation_times.append(nav_time)

            # Assert individual navigation is fast
            assert nav_time < 2000, f"{module} navigation time {nav_time}ms exceeds 2000ms"

        # Check average navigation time
        avg_time = sum(navigation_times) / len(navigation_times)
        assert avg_time < 1500, f"Average navigation time {avg_time}ms exceeds 1500ms"
