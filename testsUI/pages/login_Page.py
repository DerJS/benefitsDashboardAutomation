from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = "input[name='Username']"
        self.password_input = "input[name='Password']"
        self.login_button = "button[type='submit']"
        self.header = "header"
        self.footer = "footer"



    def open_url(self):
        self.page.goto("https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/Login")
        assert self.page.url.endswith("/Prod/Account/Login"), f"No se redirigió al login. URL actual: {page.url}"

    def login(self, username: str, password: str):
        self.page.wait_for_selector(self.username_input)
        self.page.fill(self.username_input, username)

        self.page.wait_for_selector(self.password_input)
        self.page.fill(self.password_input, password)

        self.page.wait_for_selector(self.login_button)
        self.page.click(self.login_button)

    def header_is_visible(self):
        self.page.wait_for_selector(self.header)
        assert self.page.is_visible(self.header), "Header is not visible"
    

    def footer_is_visible(self):
        self.page.wait_for_selector(self.footer)
        assert self.page.is_visible(self.footer), "Header is not visible"
