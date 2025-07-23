from testsUI.pages.login_Page import LoginPage
from testsUI.pages.dashboard_Page import DashboardPage
from testsUI.pages.add_employee_Modal import AddEmployeeModalPage
import time

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


def execute_add_employee(page):
    dashboard_page = DashboardPage(page)
    dashboard_page.header_is_visible()
    dashboard_page.footer_is_visible()
    dashboard_page.table_is_visible()
    time.sleep(1) 
    dashboard_page.click_add_employee_button()
    add_employee_Modal=AddEmployeeModalPage(page)
    add_employee_Modal.modal_is_visible()
    add_employee_Modal.fill_employee_details("Tony", "Stark", "3")
    time.sleep(1)
    add_employee_Modal.click_add_button()


def execute_logout(page):
    dashboard_page = DashboardPage(page)
    dashboard_page.click_logout()
    login_page = LoginPage(page)
    login_page.header_is_visible()
    login_page.footer_is_visible()
    login_page.login_ends("Test Case Completed")
    
