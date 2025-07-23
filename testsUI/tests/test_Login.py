from testsUI.pages.login_Page import LoginPage
from testsUI.pages.dashboard_Page import DashboardPage
import time

def test_user_can_login(page):
    login_page = LoginPage(page)
    login_page.open_url()
    login_page.header_is_visible()
    login_page.footer_is_visible()
    login_page.login("TestUser758", "mHLd_eME(#'5")
    DashboardPage.header_is_visible()
    DashboardPage.footer_is_visible()
    DashboardPage.table_is_visible()
