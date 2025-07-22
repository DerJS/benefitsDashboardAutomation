from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = "input[name='Username']"
        self.password_input = "input[name='Password']"
        self.login_button = "button[type='submit']"



    def navigate(self):
        self.page.goto("https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/Login")

    def login(self, username: str, password: str):
        self.page.wait_for_selector(self.username_input)
        self.page.fill(self.username_input, username)

        self.page.wait_for_selector(self.password_input)
        self.page.fill(self.password_input, password)

        self.page.wait_for_selector(self.login_button)
        self.page.click(self.login_button)
