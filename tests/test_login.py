from playwright.sync_api import sync_playwright, expect


class TestOrangeHRMLogin:
    def setup_method(self):
        self.url = "https://opensource-demo.orangehrmlive.com/"
        self.username = "Admin"
        self.password = "admin123"

    def test_login(self, headless=True):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=headless)
            page = browser.new_page()

            # Open login page
            page.goto(self.url)

            # Fill credentials
            page.get_by_placeholder("Username").fill(self.username)
            page.get_by_placeholder("Password").fill(self.password)

            # Click login button
            page.get_by_role("button", name="Login").click()

            # Validate dashboard
            page.wait_for_selector("text=Dashboard")
            expect(page.locator("text=Dashboard")).to_be_visible()

            print("Login test passed successfully!")

            browser.close()


if __name__ == "__main__":
    TestOrangeHRMLogin().test_login(headless=True)
