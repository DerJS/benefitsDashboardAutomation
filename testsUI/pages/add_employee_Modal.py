class AddEmployeeModalPage:
    def __init__(self, page):
        self.page = page
        self.modal_container = "#employeeModal" 
        self.first_name_input = "#firstName"
        self.last_name_input = "#lastName"
        self.dependents_input = "#dependants"
        self.add_button = "#addEmployee"
        self.confirm_delete_button = "#deleteEmployee"


    def modal_is_visible(self):
        self.page.wait_for_selector(self.modal_container,state='visible')
        assert self.page.is_visible(self.modal_container), "Add Employee Modal is not visible"

    def fill_employee_details(self, first_name: str, last_name: str, dependents: int):
        self.page.wait_for_selector(self.first_name_input)
        self.page.fill(self.first_name_input, first_name)
        self.page.wait_for_selector(self.last_name_input)
        self.page.fill(self.last_name_input, last_name)
        self.page.wait_for_selector(self.dependents_input)
        self.page.fill(self.dependents_input, str(dependents))

    def click_add_button(self): 
        self.page.wait_for_selector(self.add_button)
        self.page.click(self.add_button)

    def confirm_deleting(self):
        self.page.wait_for_selector(self.confirm_delete_button)
        self.page.click(self.confirm_delete_button)

        
        
