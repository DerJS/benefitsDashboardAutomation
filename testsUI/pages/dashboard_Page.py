class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.header = "header"
        self.dashboard_button = "a.navbar-brand"
        self.logout_button = "text=Log Out"
        self.table = "table"
        self.footer = "footer"
        self.add_employee_button = "text=Add Employee"   

    

    def header_is_visible(self):
        self.page.wait_for_selector(self.header)
        assert self.page.is_visible(self.header), "Header is not visible"

    def footer_is_visible(self):
        self.page.wait_for_selector(self.header)
        assert self.page.is_visible(self.footer), "Footer is not visible"
    
    def click_dashboard_button(self):
        self.page.wait_for_selector(self.dashboard_button)
        self.page.click(self.dashboard_button)
    
    def table_is_visible(self):
        self.page.wait_for_selector(self.table)
        assert self.page.is_visible(self.table), "Table is not visible"

    def click_logout(self):
        self.page.wait_for_selector(self.logout_button)
        self.page.click(self.logout_button)

    def click_add_employee_button(self):
        self.page.wait_for_selector(self.add_employee_button, state='visible')
        self.page.click(self.add_employee_button, force=True)

    


    