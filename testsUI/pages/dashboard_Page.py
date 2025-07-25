class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.header = "header"
        self.dashboard_button = "a.navbar-brand"
        self.logout_button = "text=Log Out"
        self.table = "table"
        self.footer = "footer"
        self.add_employee_button = "text=Add Employee"   
        self.table_row ="table tbody tr"
        self.delete_button = "td"

    

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

    def delete_employee_by_name(self, employee):
        first_name = employee['first_name']
        self.page.wait_for_selector(self.table_row)
        row = self.page.locator(f"{self.table_row}:has-text('{first_name}')").first
        row.locator("i.fa-times").click()

    def employee_is_visible(self,name):
        return self.page.locator(f"{self.table_row}:has-text('{name}')").is_visible()

        

    


    