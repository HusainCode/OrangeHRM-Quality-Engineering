from playwright.sync_api import sync_playwright, expect


class OrangeHRMLoginTest:
    def __init__(self):
        self.url = "https://opensource-demo.orangehrmlive.com/"
        self.username = "Admin"
        self.password = "admin123"

    def run_test(self, headless=False):
        pass


if __name__ == "__main__":
    OrangeHRMLoginTest().run_test(headless=False)
