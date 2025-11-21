"""
Admin Tests - User management module
Tests for adding, editing, and deleting system users.
"""
import pytest
from pages import AdminPage
from utils import assertions


@pytest.mark.regression
@pytest.mark.admin
class TestAdmin:
    """Admin module test suite"""

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
