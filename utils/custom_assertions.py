"""
Custom assertion helpers for common test scenarios.
These wrap Playwright's expect() with business-specific logic.
"""
from playwright.sync_api import Page, Locator, expect
import re


class CustomAssertions:
    """Custom assertions for OrangeHRM test scenarios"""

    @staticmethod
    def assert_on_login_page(page: Page):
        """Assert that we're on the login page"""
        expect(page).to_have_url(re.compile(r".*/auth/login"))
        expect(page.locator('.oxd-text--h5')).to_be_visible()

    @staticmethod
    def assert_on_dashboard(page: Page):
        """Assert that we're on the dashboard"""
        expect(page).to_have_url(re.compile(r".*/dashboard"))

    @staticmethod
    def assert_success_message(page: Page, message: str = None, timeout: int = 10000):
        """Assert success toast appears with optional message"""
        toast = page.locator('.oxd-toast--success')
        expect(toast).to_be_visible(timeout=timeout)
        if message:
            expect(toast).to_contain_text(message, timeout=timeout)

    @staticmethod
    def assert_error_message(page: Page, message: str = None, timeout: int = 10000):
        """Assert error toast appears with optional message"""
        toast = page.locator('.oxd-toast--error, .oxd-alert-content-text')
        expect(toast).to_be_visible(timeout=timeout)
        if message:
            expect(toast).to_contain_text(message, timeout=timeout)

    @staticmethod
    def assert_required_field_error(locator: Locator):
        """Assert that a required field error is shown"""
        error = locator.locator('..').locator('.oxd-input-field-error-message')
        expect(error).to_be_visible()
        expect(error).to_contain_text("Required")

    @staticmethod
    def assert_validation_error(page: Page, error_text: str):
        """Assert specific validation error appears"""
        error = page.locator('.oxd-input-field-error-message')
        expect(error).to_be_visible()
        expect(error).to_contain_text(error_text)

    @staticmethod
    def assert_element_visible(locator: Locator, timeout: int = 10000):
        """Assert element is visible"""
        expect(locator).to_be_visible(timeout=timeout)

    @staticmethod
    def assert_element_hidden(locator: Locator, timeout: int = 10000):
        """Assert element is hidden"""
        expect(locator).to_be_hidden(timeout=timeout)

    @staticmethod
    def assert_element_enabled(locator: Locator):
        """Assert element is enabled"""
        expect(locator).to_be_enabled()

    @staticmethod
    def assert_element_disabled(locator: Locator):
        """Assert element is disabled"""
        expect(locator).to_be_disabled()

    @staticmethod
    def assert_element_has_text(locator: Locator, text: str):
        """Assert element contains specific text"""
        expect(locator).to_contain_text(text)

    @staticmethod
    def assert_element_count(locator: Locator, count: int):
        """Assert specific number of elements"""
        expect(locator).to_have_count(count)

    @staticmethod
    def assert_url_contains(page: Page, url_part: str):
        """Assert URL contains specific string"""
        expect(page).to_have_url(re.compile(f".*{re.escape(url_part)}.*"))

    @staticmethod
    def assert_no_records_found(page: Page):
        """Assert 'No Records Found' message appears"""
        message = page.locator('.oxd-toast-content, .oxd-text')
        expect(message).to_contain_text("No Records Found", timeout=10000)

    @staticmethod
    def assert_table_row_count(page: Page, count: int, table_selector: str = '.oxd-table-card'):
        """Assert specific number of rows in table"""
        rows = page.locator(table_selector)
        expect(rows).to_have_count(count)

    @staticmethod
    def assert_table_contains_text(page: Page, text: str, table_selector: str = '.oxd-table-body'):
        """Assert table contains specific text"""
        table = page.locator(table_selector)
        expect(table).to_contain_text(text)

    @staticmethod
    def assert_dropdown_has_value(locator: Locator, value: str):
        """Assert dropdown has specific value selected"""
        expect(locator).to_have_value(value)

    @staticmethod
    def assert_checkbox_checked(locator: Locator):
        """Assert checkbox is checked"""
        expect(locator).to_be_checked()

    @staticmethod
    def assert_checkbox_unchecked(locator: Locator):
        """Assert checkbox is unchecked"""
        expect(locator).not_to_be_checked()

    @staticmethod
    def assert_page_title(page: Page, title: str):
        """Assert page has specific title"""
        expect(page).to_have_title(re.compile(title, re.IGNORECASE))

    @staticmethod
    def assert_attribute_value(locator: Locator, attribute: str, value: str):
        """Assert element has specific attribute value"""
        expect(locator).to_have_attribute(attribute, value)


# Convenience instance
assertions = CustomAssertions()
