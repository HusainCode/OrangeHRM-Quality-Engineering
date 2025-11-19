"""
Leave Page Object - handles leave management.
Includes applying leave, approving/rejecting leave requests.
"""
from playwright.sync_api import Page
from pages.base_page import BasePage


class LeavePage(BasePage):
    """Leave page object for OrangeHRM"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.path = "web/index.php/leave/viewLeaveList"
        self.apply_path = "web/index.php/leave/applyLeave"
        self.assign_path = "web/index.php/leave/assignLeave"

    # ---------- Locators ----------
    @property
    def leave_menu_link(self):
        """Leave menu link"""
        return self.page.get_by_role("link", name="Leave")

    @property
    def apply_link(self):
        """Apply leave link"""
        return self.page.get_by_role("link", name="Apply")

    @property
    def my_leave_link(self):
        """My leave link"""
        return self.page.get_by_role("link", name="My Leave")

    @property
    def leave_list_link(self):
        """Leave list link"""
        return self.page.get_by_role("link", name="Leave List")

    @property
    def assign_leave_link(self):
        """Assign leave link"""
        return self.page.get_by_role("link", name="Assign Leave")

    # Apply Leave Form
    @property
    def leave_type_dropdown(self):
        """Leave type dropdown"""
        return self.page.locator('label:text("Leave Type")').locator('..').locator('.oxd-select-text-input')

    @property
    def from_date_input(self):
        """From date input"""
        return self.page.locator('label:text("From Date")').locator('..').locator('input')

    @property
    def to_date_input(self):
        """To date input"""
        return self.page.locator('label:text("To Date")').locator('..').locator('input')

    @property
    def comments_textarea(self):
        """Comments textarea"""
        return self.page.locator('textarea').first

    @property
    def apply_button(self):
        """Apply button"""
        return self.page.get_by_role("button", name="Apply")

    @property
    def cancel_button(self):
        """Cancel button"""
        return self.page.get_by_role("button", name="Cancel")

    # Leave List and Actions
    @property
    def leave_list_table(self):
        """Leave list table"""
        return self.page.locator('.oxd-table-body')

    @property
    def leave_list_rows(self):
        """Leave list table rows"""
        return self.page.locator('.oxd-table-card')

    @property
    def approve_button(self):
        """Approve leave button (action button in table)"""
        return self.page.get_by_role("button", name="Approve")

    @property
    def reject_button(self):
        """Reject leave button (action button in table)"""
        return self.page.get_by_role("button", name="Reject")

    # Search filters
    @property
    def from_date_search_input(self):
        """From date search input"""
        return self.page.locator('.oxd-form').locator('input').first

    @property
    def to_date_search_input(self):
        """To date search input"""
        return self.page.locator('.oxd-form').locator('input').nth(1)

    @property
    def search_button(self):
        """Search button"""
        return self.page.get_by_role("button", name="Search")

    @property
    def reset_button(self):
        """Reset button"""
        return self.page.get_by_role("button", name="Reset")

    # ---------- Actions ----------
    def navigate(self):
        """Navigate to leave list"""
        self.navigate_to(self.path)

    def navigate_to_apply_leave(self):
        """Navigate to apply leave page"""
        self.click_menu_item("Leave")
        self.apply_link.click()

    def navigate_to_my_leave(self):
        """Navigate to my leave page"""
        self.click_menu_item("Leave")
        self.my_leave_link.click()

    def navigate_to_leave_list(self):
        """Navigate to leave list page"""
        self.click_menu_item("Leave")
        self.leave_list_link.click()

    def select_leave_type(self, leave_type: str):
        """Select leave type from dropdown"""
        self.leave_type_dropdown.click()
        self.page.get_by_role("option", name=leave_type).click()

    def enter_from_date(self, date: str):
        """Enter from date (YYYY-MM-DD format)"""
        self.from_date_input.fill(date)

    def enter_to_date(self, date: str):
        """Enter to date (YYYY-MM-DD format)"""
        self.to_date_input.fill(date)

    def enter_comments(self, comments: str):
        """Enter leave comments"""
        self.comments_textarea.fill(comments)

    def click_apply(self):
        """Click apply button"""
        self.apply_button.click()

    def apply_leave(self, leave_type: str, from_date: str, to_date: str, comments: str = ""):
        """Apply for leave with required fields"""
        self.select_leave_type(leave_type)
        self.enter_from_date(from_date)
        self.enter_to_date(to_date)
        if comments:
            self.enter_comments(comments)
        self.click_apply()

    def approve_first_leave(self):
        """Approve the first leave in the list"""
        self.approve_button.first.click()

    def reject_first_leave(self):
        """Reject the first leave in the list"""
        self.reject_button.first.click()

    def search_leave_by_date(self, from_date: str, to_date: str):
        """Search leave by date range"""
        self.from_date_search_input.fill(from_date)
        self.to_date_search_input.fill(to_date)
        self.search_button.click()

    def reset_search(self):
        """Reset search filters"""
        self.reset_button.click()

    def get_leave_count(self) -> int:
        """Get number of leave records in table"""
        return self.leave_list_rows.count()

    def get_leave_status(self, row_index: int = 0) -> str:
        """Get leave status from specific row"""
        return self.leave_list_rows.nth(row_index).locator('.oxd-table-cell').nth(5).text_content()
