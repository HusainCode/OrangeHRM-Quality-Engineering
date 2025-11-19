"""
Admin Tests - User management module
Tests for adding, editing, and deleting system users.
"""
import pytest
from pages import AdminPage
from utils import assertions, waits, data


@pytest.mark.regression
@pytest.mark.admin
class TestAdmin:
    """Admin module test suite"""

    @pytest.mark.skip(reason="Requires actual employee to exist for user creation")
    def test_add_user_with_valid_data(
        self, authenticated_admin_page: AdminPage, random_user_data: dict
    ):
        """
        Test ID: ADMIN-ADD-001
        Verify that system user can be created with valid data
        Note: This test requires an existing employee record
        """
        admin = authenticated_admin_page

        # Navigate to add user
        admin.navigate()
        admin.click_add_user()

        # Add user (requires existing employee name like "Peter Mac Anderson")
        admin.add_user(
            role=random_user_data["role"],
            employee_name="Peter",  # Partial name for autocomplete
            status=random_user_data["status"],
            username=random_user_data["username"],
            password=random_user_data["password"]
        )

        # Assert success
        waits.wait_for_success_toast(admin.page)
        assertions.assert_success_message(admin.page)

    @pytest.mark.skip(reason="Requires existing user to delete")
    def test_delete_user_removes_from_list(self, authenticated_admin_page: AdminPage):
        """
        Test ID: ADMIN-DEL-001
        Verify that deleted user is removed from the system
        """
        admin = authenticated_admin_page

        admin.navigate()
        waits.wait_for_network_idle(admin.page)

        # Search for a specific user (adjust username as needed)
        test_username = "testuser123"
        admin.search_user_by_username(test_username)
        waits.wait_for_network_idle(admin.page)

        # Delete if found
        if admin.get_user_count() > 0:
            admin.select_user_checkbox(0)
            admin.delete_selected_user()
            waits.wait_for_success_toast(admin.page)

            # Verify deleted
            admin.search_user_by_username(test_username)
            waits.wait_for_network_idle(admin.page)
            assertions.assert_no_records_found(admin.page)

    def test_add_user_requires_all_fields(self, authenticated_admin_page: AdminPage):
        """
        Test ID: ADMIN-VAL-001
        Verify validation when required fields are missing
        """
        admin = authenticated_admin_page

        admin.navigate()
        admin.click_add_user()

        # Try to save without filling fields
        admin.click_save()

        # Assert validation errors appear
        assertions.assert_element_visible(admin.required_error)
