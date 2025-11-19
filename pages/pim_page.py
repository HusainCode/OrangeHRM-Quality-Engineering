"""
PIM (Personnel Information Management) Page Object.
Handles employee management: add, search, edit, delete employees.
"""
from playwright.sync_api import Page
from pages.base_page import BasePage


class PimPage(BasePage):
    """PIM page object for OrangeHRM"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.path = "web/index.php/pim/viewEmployeeList"
        self.add_employee_path = "web/index.php/pim/addEmployee"

    # ---------- Navigation ----------
    def navigate(self):
        """Navigate to employee list"""
        self.navigate_to(self.path)

    def navigate_to_add_employee(self):
        """Navigate to Add Employee page via menu"""
        self.click_menu_item("PIM")
        self.add_employee_link.click()

    def navigate_to_add_employee_direct(self):
        """Navigate directly to Add Employee page"""
        self.navigate_to(self.add_employee_path)

    # ---------- Locators ----------
    # PIM Menu
    @property
    def pim_menu_link(self):
        return self.page.get_by_role("link", name="PIM")

    @property
    def add_employee_link(self):
        return self.page.get_by_role("link", name="Add Employee")

    # Add Employee Form
    @property
    def first_name_input(self):
        return self.page.locator('input[name="firstName"]')

    @property
    def middle_name_input(self):
        return self.page.locator('input[name="middleName"]')

    @property
    def last_name_input(self):
        return self.page.locator('input[name="lastName"]')

    @property
    def employee_id_input(self):
        return self.page.locator('.oxd-grid').locator('input').nth(4)

    @property
    def save_button(self):
        return self.page.get_by_role("button", name="Save")

    @property
    def cancel_button(self):
        return self.page.get_by_role("button", name="Cancel")

    # Success/Error Messages
    @property
    def success_toast(self):
        return self.page.locator('.oxd-toast--success')

    @property
    def error_toast(self):
        return self.page.locator('.oxd-toast--error')

    @property
    def required_field_error(self):
        return self.page.locator('.oxd-input-field-error-message').first

    @property
    def first_name_required_error(self):
        return self.first_name_input.locator('..').locator('..').locator('.oxd-input-field-error-message')

    @property
    def last_name_required_error(self):
        return self.last_name_input.locator('..').locator('..').locator('.oxd-input-field-error-message')

    # Employee List
    @property
    def employee_name_search_input(self):
        return self.page.locator('input[placeholder*="Type for hints"]').first

    @property
    def employee_id_search_input(self):
        return self.page.locator('.oxd-grid').locator('input').nth(1)

    @property
    def search_button(self):
        return self.page.get_by_role("button", name="Search")

    @property
    def reset_button(self):
        return self.page.get_by_role("button", name="Reset")

    @property
    def employee_table(self):
        return self.page.locator('.oxd-table-body')

    @property
    def employee_table_rows(self):
        return self.page.locator('.oxd-table-card')

    @property
    def delete_button(self):
        return self.page.get_by_role("button", name="Delete Selected")

    @property
    def confirm_delete_button(self):
        return self.page.get_by_role("button", name="Yes, Delete")

    # ---------- Actions ----------
    def enter_first_name(self, first_name: str):
        """Enter first name"""
        self.first_name_input.fill(first_name)

    def enter_middle_name(self, middle_name: str):
        """Enter middle name"""
        self.middle_name_input.fill(middle_name)

    def enter_last_name(self, last_name: str):
        """Enter last name"""
        self.last_name_input.fill(last_name)

    def enter_employee_id(self, employee_id: str):
        """Enter employee ID"""
        self.employee_id_input.clear()
        self.employee_id_input.fill(employee_id)

    def click_save(self):
        """Click save button"""
        self.save_button.click()

    def add_employee(self, first_name: str, last_name: str, middle_name: str = "", employee_id: str = ""):
        """Add a new employee with required fields"""
        self.enter_first_name(first_name)
        if middle_name:
            self.enter_middle_name(middle_name)
        self.enter_last_name(last_name)
        if employee_id:
            self.enter_employee_id(employee_id)
        self.click_save()

    def search_employee_by_name(self, full_name: str):
        """Search for an employee by name in the employee list"""
        self.employee_name_search_input.fill(full_name)
        self.search_button.click()

    def search_employee_by_id(self, employee_id: str):
        """Search for an employee by ID in the employee list"""
        self.employee_id_search_input.fill(employee_id)
        self.search_button.click()

    def reset_search(self):
        """Reset the search filters"""
        self.reset_button.click()

    def select_employee_checkbox(self, row_index: int = 0):
        """Select an employee checkbox by row index (default first row)"""
        self.employee_table_rows.nth(row_index).locator('.oxd-checkbox-input').click()

    def delete_selected_employee(self):
        """Click delete button and confirm deletion"""
        self.delete_button.click()
        self.confirm_delete_button.click()

    def get_employee_count(self) -> int:
        """Get the number of employees in the table"""
        return self.employee_table_rows.count()

    def get_employee_id_value(self) -> str:
        """Get the auto-generated employee ID value"""
        return self.employee_id_input.input_value()

    def is_on_add_employee_page(self) -> bool:
        """Check if on Add Employee page"""
        return "/pim/addEmployee" in self.page.url

