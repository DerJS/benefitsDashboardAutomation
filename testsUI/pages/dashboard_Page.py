class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.header = "header"
        self.dashboard_button = "header >> text:Paylocity  Dashboard"
        self.logout_button = "header >> text=Log Out"
        self.table = "table"
        self.footer = "footer"
       

    

    def header_is_visible(self):
        self.page.wait_for_selector(self.header)
        assert self.page.is_visible(self.header), "Header is not visible"

    def footer_is_visible(self):
        self.page.wait_for_selector(self.header)
        assert self.page.is_visible(self.footer), "Footer is not visible"
    
    def click_dashboard_button(self):
        self.page.click(self.dashboard_button)
    
    def table_is_visible(self):
        self.page.wait_for_selector(self.table)
        assert self.page.is_visible(self.table), "Table is not visible"

    def click_logout(self):
        self.page.wait_for_selector(self.logout_button)
        self.page.click(self.logout_button)

    