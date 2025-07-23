from testsUI.pages.login_Page import LoginPage
from testsUI.pages.dashboard_Page import DashboardPage

def execute_login(page):
    login_page = LoginPage(page)
    login_page.open_url()
    login_page.header_is_visible()
    login_page.footer_is_visible()
    login_page.login("TestUser758", "mHLd_eME(#'5")

    dashboard_page = DashboardPage(page)
    dashboard_page.header_is_visible()
    dashboard_page.footer_is_visible()
    dashboard_page.table_is_visible()

def execute_logout(page):
    dashboard_page = DashboardPage(page)
    dashboard_page.click_dashboard_button()
    dashboard_page.click_logout()
    login_page = LoginPage(page)
    login_page.header_is_visible()
    login_page.footer_is_visible()
    
