from playwright.sync_api import Page, expect


class PimPage:
    URL_PIM = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"

    def __init__(self, pimPage: Page):
        self.page = pimPage

    # ---------- Navigation ----------
    def navigate(self):
        self.page.goto(self.URL_PIM)

    def navigate_to_add_employee(self):
        """Navigate to Add Employee page via PIM menu"""
        self.page.get_by_role("link", name="PIM").click()
        self.page.get_by_role("link", name="Add Employee").click()

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
    def add_employee(self, first_name: str, last_name: str, middle_name: str = "", employee_id: str = ""):
        """Add a new employee with required fields"""
        self.first_name_input.fill(first_name)
        if middle_name:
            self.middle_name_input.fill(middle_name)
        self.last_name_input.fill(last_name)
        if employee_id:
            self.employee_id_input.clear()
            self.employee_id_input.fill(employee_id)
        self.save_button.click()

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
        self.employee_table_rows.nth(row_index).locator('input[type="checkbox"]').check()

    def delete_selected_employee(self):
        """Click delete button and confirm deletion"""
        self.delete_button.click()
        self.confirm_delete_button.click()

    def get_employee_count(self):
        """Get the number of employees in the table"""
        return self.employee_table_rows.count()

    # ---------- Assertions ----------
    def assert_success_toast_visible(self):
        """Assert that success toast message is visible"""
        expect(self.success_toast).to_be_visible()

    def assert_error_toast_visible(self):
        """Assert that error toast message is visible"""
        expect(self.error_toast).to_be_visible()

    def assert_required_field_error_visible(self):
        """Assert that required field error message is visible"""
        expect(self.required_field_error).to_be_visible()

    def assert_employee_in_list(self, employee_name: str):
        """Assert that an employee appears in the search results"""
        expect(self.employee_table).to_contain_text(employee_name)

    def assert_employee_not_in_list(self):
        """Assert that no records are found"""
        expect(self.page.locator('.oxd-toast, .oxd-table-cell')).to_contain_text("No Records Found")

    def assert_on_add_employee_page(self):
        """Assert that we're on the Add Employee page"""
        import re
        expect(self.page).to_have_url(re.compile(r".*/pim/addEmployee"))

