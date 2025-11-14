from playwright.sync_api import Page , expect


class LoginPage:
    URL = "https://opensource-demo.orangehrmlive.com/"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto(self.URL)
    