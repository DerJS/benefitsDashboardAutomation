from testsUI.pages.login_Page import LoginPage

def test_user_can_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("TestUser758", "mHLd_eME(#'5")

  