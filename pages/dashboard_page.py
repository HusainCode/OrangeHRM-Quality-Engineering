"""
Dashboard Page Object - handles dashboard interactions.
Dashboard is the landing page after successful login.
"""
from playwright.sync_api import Page
from pages.base_page import BasePage


class DashboardPage(BasePage):
    """Dashboard page object for OrangeHRM"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.path = "web/index.php/dashboard/index"

    # ---------- Locators ----------
    @property
    def dashboard_title(self):
        """Dashboard page title"""
        return self.page.locator("h6").filter(has_text="Dashboard")

    @property
    def time_at_work_widget(self):
        """Time at Work widget"""
        return self.page.locator('.orangehrm-dashboard-widget').filter(has_text="Time at Work")

    @property
    def my_actions_widget(self):
        """My Actions widget"""
        return self.page.locator('.orangehrm-dashboard-widget').filter(has_text="My Actions")

    @property
    def quick_launch_widget(self):
        """Quick Launch widget"""
        return self.page.locator('.orangehrm-dashboard-widget').filter(has_text="Quick Launch")

    @property
    def buzz_latest_posts_widget(self):
        """Buzz Latest Posts widget"""
        return self.page.locator('.orangehrm-dashboard-widget').filter(has_text="Buzz Latest Posts")

    @property
    def employees_on_leave_widget(self):
        """Employees on Leave Today widget"""
        return self.page.locator('.orangehrm-dashboard-widget').filter(has_text="Employees on Leave Today")

    @property
    def employee_distribution_widget(self):
        """Employee Distribution by Sub Unit widget"""
        return self.page.locator('.orangehrm-dashboard-widget').filter(has_text="Employee Distribution")

    @property
    def leave_quick_launch_button(self):
        """Assign Leave quick launch button"""
        return self.page.get_by_role("button", name="Assign Leave")

    @property
    def leave_list_quick_launch_button(self):
        """Leave List quick launch button"""
        return self.page.get_by_role("button", name="Leave List")

    @property
    def timesheets_quick_launch_button(self):
        """Timesheets quick launch button"""
        return self.page.get_by_role("button", name="Timesheets")

    @property
    def apply_leave_quick_launch_button(self):
        """Apply Leave quick launch button"""
        return self.page.get_by_role("button", name="Apply Leave")

    @property
    def my_leave_quick_launch_button(self):
        """My Leave quick launch button"""
        return self.page.get_by_role("button", name="My Leave")

    @property
    def my_timesheet_quick_launch_button(self):
        """My Timesheet quick launch button"""
        return self.page.get_by_role("button", name="My Timesheet")

    # ---------- Actions ----------
    def navigate(self):
        """Navigate to dashboard"""
        self.navigate_to(self.path)

    def click_assign_leave(self):
        """Click Assign Leave quick action"""
        self.leave_quick_launch_button.click()

    def click_leave_list(self):
        """Click Leave List quick action"""
        self.leave_list_quick_launch_button.click()

    def click_timesheets(self):
        """Click Timesheets quick action"""
        self.timesheets_quick_launch_button.click()

    def click_apply_leave(self):
        """Click Apply Leave quick action"""
        self.apply_leave_quick_launch_button.click()

    def click_my_leave(self):
        """Click My Leave quick action"""
        self.my_leave_quick_launch_button.click()

    def click_my_timesheet(self):
        """Click My Timesheet quick action"""
        self.my_timesheet_quick_launch_button.click()

    def is_page_loaded(self) -> bool:
        """Check if dashboard is loaded"""
        return self.dashboard_title.is_visible()

    def get_widget_count(self) -> int:
        """Count number of widgets on dashboard"""
        return self.page.locator('.orangehrm-dashboard-widget').count()
