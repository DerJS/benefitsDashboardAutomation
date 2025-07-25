from testsUI.pages.login_Page import LoginPage
from testsUI.pages.dashboard_Page import DashboardPage
from testsUI.tests.helpers.helpers import execute_login, execute_logout, execute_add_employee, execute_delete_employee

def test_Standard_Workflow(page):
    execute_login(page)
    employee=execute_add_employee(page)
    execute_delete_employee(page, employee)
    execute_logout(page)
