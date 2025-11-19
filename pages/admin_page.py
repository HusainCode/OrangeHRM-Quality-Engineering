"""
Admin Page Object - handles user management.
Admin module manages system users, job titles, locations, etc.
"""
from playwright.sync_api import Page
from pages.base_page import BasePage


class AdminPage(BasePage):
    """Admin page object for OrangeHRM"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.path = "web/index.php/admin/viewSystemUsers"
        self.add_user_path = "web/index.php/admin/saveSystemUser"

    # ---------- Locators ----------
    @property
    def admin_menu_link(self):
        """Admin menu link"""
        return self.page.get_by_role("link", name="Admin")

    @property
    def add_button(self):
        """Add user button"""
        return self.page.get_by_role("button", name="Add")

    # User Form Fields
    @property
    def user_role_dropdown(self):
        """User role dropdown"""
        return self.page.locator('label:text("User Role")').locator('..').locator('.oxd-select-text-input')

    @property
    def employee_name_input(self):
        """Employee name autocomplete input"""
        return self.page.locator('label:text("Employee Name")').locator('..').locator('input')

    @property
    def status_dropdown(self):
        """Status dropdown"""
        return self.page.locator('label:text("Status")').locator('..').locator('.oxd-select-text-input')

    @property
    def username_input(self):
        """Username input field"""
        return self.page.locator('label:text("Username")').locator('..').locator('input').nth(0)

    @property
    def password_input(self):
        """Password input field"""
        return self.page.locator('label:text("Password")').locator('..').locator('input').nth(0)

    @property
    def confirm_password_input(self):
        """Confirm password input field"""
        return self.page.locator('label:text("Confirm Password")').locator('..').locator('input').nth(0)

    @property
    def save_button(self):
        """Save button"""
        return self.page.get_by_role("button", name="Save")

    @property
    def cancel_button(self):
        """Cancel button"""
        return self.page.get_by_role("button", name="Cancel")

    # Search and Table
    @property
    def username_search_input(self):
        """Username search input"""
        return self.page.locator('label:text("Username")').locator('..').locator('input')

    @property
    def user_role_search_dropdown(self):
        """User role search dropdown"""
        return self.page.locator('.oxd-form').locator('.oxd-select-text-input').first

    @property
    def employee_name_search_input(self):
        """Employee name search input"""
        return self.page.locator('input[placeholder*="Type for hints"]').first

    @property
    def status_search_dropdown(self):
        """Status search dropdown"""
        return self.page.locator('.oxd-form').locator('.oxd-select-text-input').nth(1)

    @property
    def search_button(self):
        """Search button"""
        return self.page.get_by_role("button", name="Search")

    @property
    def reset_button(self):
        """Reset button"""
        return self.page.get_by_role("button", name="Reset")

    @property
    def users_table(self):
        """Users table"""
        return self.page.locator('.oxd-table-body')

    @property
    def users_table_rows(self):
        """User table rows"""
        return self.page.locator('.oxd-table-card')

    @property
    def delete_button(self):
        """Delete selected button"""
        return self.page.get_by_role("button", name="Delete Selected")

    @property
    def confirm_delete_button(self):
        """Confirm delete button"""
        return self.page.get_by_role("button", name="Yes, Delete")

    # Error messages
    @property
    def required_error(self):
        """Required field error"""
        return self.page.locator('.oxd-input-field-error-message').first

    # ---------- Actions ----------
    def navigate(self):
        """Navigate to admin page"""
        self.navigate_to(self.path)

    def click_add_user(self):
        """Click add user button"""
        self.add_button.click()

    def select_user_role(self, role: str):
        """Select user role from dropdown (Admin or ESS)"""
        self.user_role_dropdown.click()
        self.page.get_by_role("option", name=role).click()

    def enter_employee_name(self, name: str):
        """Enter employee name and select from autocomplete"""
        self.employee_name_input.fill(name)
        self.page.wait_for_timeout(1000)  # Wait for autocomplete
        self.page.get_by_role("option").first.click()

    def select_status(self, status: str):
        """Select status from dropdown (Enabled or Disabled)"""
        self.status_dropdown.click()
        self.page.get_by_role("option", name=status).click()

    def enter_username(self, username: str):
        """Enter username"""
        self.username_input.fill(username)

    def enter_password(self, password: str):
        """Enter password"""
        self.password_input.fill(password)

    def enter_confirm_password(self, password: str):
        """Enter confirm password"""
        self.confirm_password_input.fill(password)

    def click_save(self):
        """Click save button"""
        self.save_button.click()

    def add_user(self, role: str, employee_name: str, status: str, username: str, password: str):
        """Add a new user with all required fields"""
        self.select_user_role(role)
        self.enter_employee_name(employee_name)
        self.select_status(status)
        self.enter_username(username)
        self.enter_password(password)
        self.enter_confirm_password(password)
        self.click_save()

    def search_user_by_username(self, username: str):
        """Search for a user by username"""
        self.username_search_input.fill(username)
        self.search_button.click()

    def reset_search(self):
        """Reset search filters"""
        self.reset_button.click()

    def select_user_checkbox(self, row_index: int = 0):
        """Select user checkbox by row index"""
        self.users_table_rows.nth(row_index).locator('.oxd-checkbox-input').click()

    def delete_selected_user(self):
        """Delete selected user"""
        self.delete_button.click()
        self.confirm_delete_button.click()

    def get_user_count(self) -> int:
        """Get number of users in table"""
        return self.users_table_rows.count()

    def user_exists_in_table(self, username: str) -> bool:
        """Check if username exists in table"""
        return username in self.users_table.text_content()
