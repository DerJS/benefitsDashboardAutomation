from testsUI.pages.login_Page import LoginPage
from testsUI.pages.dashboard_Page import DashboardPage
from testsUI.tests.helpers.helpers import execute_login, execute_logout

def test_user_can_login_logout(page):
    execute_login(page)
    execute_logout(page)


    