"""
PIM Tests - Employee management module
Tests for adding, searching, editing, and deleting employees.
"""
import pytest
from pages import PimPage
from utils import assertions, waits, data


@pytest.mark.regression
@pytest.mark.pim
class TestPIM:
    """PIM module test suite"""

    def test_create_employee_with_minimum_fields(
        self, authenticated_pim_page: PimPage, random_employee_data: dict
    ):
        """
        Test ID: PIM-ADD-001
        Verify that employee can be created with minimum required fields
        """
        pim = authenticated_pim_page

        # Navigate to add employee page
        pim.navigate_to_add_employee()
        assert pim.is_on_add_employee_page(), "Should be on Add Employee page"

        # Add employee with random data
        pim.add_employee(
            random_employee_data["first_name"],
            random_employee_data["last_name"]
        )

        # Assert success
        waits.wait_for_success_toast(pim.page)
        assertions.assert_success_message(pim.page)

    def test_save_blocked_when_required_field_missing(self, authenticated_pim_page: PimPage):
        """
        Test ID: PIM-VAL-001
        Verify that save is blocked when required field is missing
        """
        pim = authenticated_pim_page

        # Navigate and try to save with missing last name
        pim.navigate_to_add_employee()
        pim.enter_first_name(data.random_first_name())
        pim.click_save()

        # Assert validation error
        assertions.assert_element_visible(pim.last_name_required_error)

    def test_new_employee_appears_in_search(
        self, authenticated_pim_page: PimPage, random_employee_data: dict
    ):
        """
        Test ID: PIM-LIST-001
        Verify that newly created employee appears in search results
        """
        pim = authenticated_pim_page

        # Create employee
        pim.navigate_to_add_employee()
        pim.add_employee(
            random_employee_data["first_name"],
            random_employee_data["last_name"]
        )

        # Wait for save (toast may appear)
        try:
            waits.wait_for_success_toast(pim.page)
        except:
            # If toast doesn't appear, just wait for network
            waits.wait_for_network_idle(pim.page)

        # Search for employee
        pim.navigate()
        waits.wait_for_network_idle(pim.page)

        pim.search_employee_by_name(random_employee_data["full_name"])
        waits.wait_for_network_idle(pim.page)

        # Assert employee appears in list
        assertions.assert_table_contains_text(pim.page, random_employee_data["first_name"])

    def test_delete_employee_removes_from_list(
        self, authenticated_pim_page: PimPage, random_employee_data: dict
    ):
        """
        Test ID: PIM-DEL-001
        Verify that deleted employee is removed from list
        """
        pim = authenticated_pim_page

        # Create employee first
        pim.navigate_to_add_employee()
        pim.add_employee(
            random_employee_data["first_name"],
            random_employee_data["last_name"]
        )
        waits.wait_for_success_toast(pim.page)

        # Search and delete
        pim.navigate()
        waits.wait_for_network_idle(pim.page)

        pim.search_employee_by_name(random_employee_data["full_name"])
        waits.wait_for_network_idle(pim.page)

        # Verify employee exists before deleting
        assertions.assert_table_contains_text(pim.page, random_employee_data["first_name"])

        # Delete employee
        pim.select_employee_checkbox(0)
        pim.delete_selected_employee()

        # Wait for deletion to complete (toast may or may not appear)
        waits.wait_for_network_idle(pim.page)

        # Verify employee is gone
        pim.reset_search()
        waits.wait_for_network_idle(pim.page)
        pim.search_employee_by_name(random_employee_data["full_name"])
        waits.wait_for_network_idle(pim.page)

        assertions.assert_no_records_found(pim.page)
