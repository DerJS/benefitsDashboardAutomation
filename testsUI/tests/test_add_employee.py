from testsUI.pages.login_Page import LoginPage
from testsUI.pages.dashboard_Page import DashboardPage
from testsUI.tests.helpers.helpers import execute_login, execute_logout, execute_add_employee

def test_user_adds_an_employee(page):
    execute_login(page)
    execute_add_employee(page)
    execute_logout(page)