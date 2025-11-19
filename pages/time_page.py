"""
Time Page Object - handles timesheet management.
Includes viewing and submitting timesheets.
"""
from playwright.sync_api import Page
from pages.base_page import BasePage


class TimePage(BasePage):
    """Time page object for OrangeHRM"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.path = "web/index.php/time/viewEmployeeTimesheet"
        self.my_timesheet_path = "web/index.php/time/viewMyTimesheet"

    # ---------- Locators ----------
    @property
    def time_menu_link(self):
        """Time menu link"""
        return self.page.get_by_role("link", name="Time")

    @property
    def timesheets_link(self):
        """Timesheets link"""
        return self.page.get_by_role("link", name="Timesheets")

    @property
    def my_timesheets_link(self):
        """My timesheets link"""
        return self.page.get_by_role("link", name="My Timesheets")

    @property
    def edit_button(self):
        """Edit timesheet button"""
        return self.page.get_by_role("button", name="Edit")

    @property
    def submit_button(self):
        """Submit timesheet button"""
        return self.page.get_by_role("button", name="Submit")

    @property
    def save_button(self):
        """Save timesheet button"""
        return self.page.get_by_role("button", name="Save")

    @property
    def reset_button(self):
        """Reset button"""
        return self.page.get_by_role("button", name="Reset")

    @property
    def timesheet_table(self):
        """Timesheet table"""
        return self.page.locator('.orangehrm-timesheet-table')

    @property
    def timesheet_status(self):
        """Timesheet status indicator"""
        return self.page.locator('.orangehrm-timesheet-status')

    @property
    def project_input(self):
        """Project input (first row)"""
        return self.page.locator('input[placeholder*="Type for hints"]').first

    @property
    def activity_dropdown(self):
        """Activity dropdown"""
        return self.page.locator('.oxd-select-text-input').first

    @property
    def add_row_button(self):
        """Add timesheet row button"""
        return self.page.get_by_role("button", name="Add Row")

    # ---------- Actions ----------
    def navigate(self):
        """Navigate to timesheets"""
        self.navigate_to(self.path)

    def navigate_to_my_timesheet(self):
        """Navigate to my timesheet"""
        self.click_menu_item("Time")
        self.my_timesheets_link.click()

    def click_edit(self):
        """Click edit timesheet button"""
        self.edit_button.click()

    def click_submit(self):
        """Click submit timesheet button"""
        self.submit_button.click()

    def click_save(self):
        """Click save timesheet button"""
        self.save_button.click()

    def add_timesheet_row(self):
        """Add a new timesheet row"""
        self.add_row_button.click()

    def enter_project(self, project_name: str):
        """Enter project name and select from autocomplete"""
        self.project_input.fill(project_name)
        self.page.wait_for_timeout(1000)
        self.page.get_by_role("option").first.click()

    def select_activity(self, activity: str):
        """Select activity from dropdown"""
        self.activity_dropdown.click()
        self.page.get_by_role("option", name=activity).click()

    def enter_hours(self, day_index: int, hours: str):
        """Enter hours for a specific day (0-6 for Mon-Sun)"""
        # Timesheet has input fields for each day
        inputs = self.page.locator('input[type="text"]').filter(has_not_text="Type for hints")
        inputs.nth(day_index).fill(hours)

    def submit_timesheet(self):
        """Submit the timesheet"""
        self.click_submit()

    def save_timesheet(self):
        """Save the timesheet"""
        self.click_save()

    def get_timesheet_status(self) -> str:
        """Get current timesheet status"""
        return self.timesheet_status.text_content()

    def is_timesheet_editable(self) -> bool:
        """Check if timesheet is in editable state"""
        return self.save_button.is_visible()
