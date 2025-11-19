import pytest
import re
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.pim_page import PimPage


@pytest.fixture
def authenticated_page(page):
    """Login before each test"""
    login = LoginPage(page)
    login.navigate()
    login.login("Admin", "admin123")
    expect(page).to_have_url(re.compile("/dashboard"))
    return page


# ---------------------------
# PIM-ADD-001: Create employee with minimum fields
# ---------------------------
def test_create_employee_min_fields(authenticated_page):
    pim = PimPage(authenticated_page)

    pim.navigate_to_add_employee()
    pim.assert_on_add_employee_page()

    pim.add_employee("John", "Doe")

    pim.assert_success_toast_visible()


# ---------------------------
# PIM-VAL-001: Validation - required field missing
# ---------------------------
def test_save_blocked_missing_required_field(authenticated_page):
    pim = PimPage(authenticated_page)

    pim.navigate_to_add_employee()

    # fill only first name, leave last name empty
    pim.first_name_input.fill("Jane")
    pim.save_button.click()

    pim.assert_required_field_error_visible()


# ---------------------------
# PIM-LIST-001: New employee appears in search
# ---------------------------
def test_new_employee_appears_in_search(authenticated_page):
    pim = PimPage(authenticated_page)

    # add new employee
    pim.navigate_to_add_employee()
    pim.add_employee("Michael", "Smith")
    pim.assert_success_toast_visible()

    # go back to employee list and search
    pim.navigate()
    authenticated_page.wait_for_load_state("networkidle")

    pim.search_employee_by_name("Michael Smith")
    authenticated_page.wait_for_timeout(1000)

    pim.assert_employee_in_list("Michael")


# ---------------------------
# PIM-DEL-001: Delete employee
# ---------------------------
def test_delete_employee(authenticated_page):
    pim = PimPage(authenticated_page)

    # first add an employee to delete
    pim.navigate_to_add_employee()
    pim.add_employee("ToDelete", "TestUser")
    pim.assert_success_toast_visible()

    # search for the employee
    pim.navigate()
    authenticated_page.wait_for_load_state("networkidle")
    authenticated_page.wait_for_timeout(1500)

    pim.search_employee_by_name("ToDelete TestUser")
    authenticated_page.wait_for_timeout(2000)

    # make sure employee appears before deleting
    pim.assert_employee_in_list("ToDelete")

    # delete the employee
    pim.select_employee_checkbox(0)
    pim.delete_selected_employee()
    authenticated_page.wait_for_timeout(1000)

    pim.assert_success_toast_visible()

    # verify employee is gone
    authenticated_page.wait_for_timeout(1000)
    pim.reset_search()
    authenticated_page.wait_for_timeout(1000)
    pim.search_employee_by_name("ToDelete TestUser")
    authenticated_page.wait_for_timeout(2000)

    pim.assert_employee_not_in_list()
