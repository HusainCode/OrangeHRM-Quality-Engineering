"""
Dashboard Tests - Dashboard widgets and quick actions
Tests for dashboard functionality and quick launch actions.
"""
import pytest
from pages import DashboardPage
from utils import assertions


@pytest.mark.regression
@pytest.mark.dashboard
class TestDashboard:
    """Dashboard test suite"""

    def test_dashboard_widgets_load_successfully(self, authenticated_dashboard_page: DashboardPage):
        """
        Test ID: DASH-001
        Verify that dashboard widgets load successfully after login
        """
        dashboard = authenticated_dashboard_page

        # Verify dashboard elements are visible
        assertions.assert_element_visible(dashboard.dashboard_title)

        # Check that at least some widgets are present
        widget_count = dashboard.get_widget_count()
        assert widget_count > 0, f"Expected widgets to load, found {widget_count}"

    def test_quick_launch_apply_leave_navigates_correctly(
        self, authenticated_dashboard_page: DashboardPage
    ):
        """
        Test ID: DASH-QA-001
        Verify that Apply Leave quick action navigates to leave application page
        """
        dashboard = authenticated_dashboard_page

        # Click Apply Leave quick action
        dashboard.click_apply_leave()

        # Verify navigation to leave page
        assertions.assert_url_contains(dashboard.page, "/leave/applyLeave")

    def test_quick_launch_my_leave_navigates_correctly(
        self, authenticated_dashboard_page: DashboardPage
    ):
        """
        Test ID: DASH-QA-002
        Verify that My Leave quick action navigates to my leave page
        """
        dashboard = authenticated_dashboard_page

        # Click My Leave quick action
        dashboard.click_my_leave()

        # Verify navigation
        assertions.assert_url_contains(dashboard.page, "/leave")

    def test_quick_launch_my_timesheet_navigates_correctly(
        self, authenticated_dashboard_page: DashboardPage
    ):
        """
        Test ID: DASH-QA-003
        Verify that My Timesheet quick action navigates to timesheet page
        """
        dashboard = authenticated_dashboard_page

        # Click My Timesheet quick action
        dashboard.click_my_timesheet()

        # Verify navigation
        assertions.assert_url_contains(dashboard.page, "/time")
