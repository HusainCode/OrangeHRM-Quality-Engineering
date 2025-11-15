import pytest
import re
from playwright.sync_api import expect
from pages.login_page import LoginPage



# ---------------------------
# VALID LOGIN TEST
# ---------------------------
def test_valid_login(page):
    login = LoginPage(page)

    login.navigate()
    
    #login.login(USERNAME, PASSWORD)  # use global credentials so tests don't break if login changes
    login.login("Admin", "admin123") 

    expect(page).to_have_url(re.compile("/dashboard"))
 


# ---------------------------
# INVALID LOGIN TESTS (DATA-DRIVEN)
# ---------------------------
@pytest.mark.parametrize(
    "username,password",
    [
        ("WrongUser", "admin123"),
        ("Admin", "wrongpass"),
        ("", "admin123"),
        ("Admin", ""),
        ("", ""),
    ]
)
def test_invalid_login(page, username, password):
    login = LoginPage(page)

    login.navigate()
    login.login(username, password)

    login.assert_login_error()
