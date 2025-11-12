from playwright.sync_api import sync_playwright, expect


class TestOrangeHRMLogin:
    def setup_method(self):
        self.url = "https://opensource-demo.orangehrmlive.com/"
        self.username = "Admin"
        self.password = "admin123"

    def test_login(self, headless=True):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto(self.url)

            page.get_by_placeholder("Username").fill(self.password)
            page.get_by_placeholder("Password").fill(self.password)
            page.get_by_role("button", name="Login").click()

            page.wait_for_selector("text=Dashboard")
            expect(page.locator("text=Dashboard")).to_be_visible()

            print("Login test passed successfully!")

            browser.close()
            

if __name__ == "__main__":
    TestOrangeHRMLogin().test_login(headless=False)
