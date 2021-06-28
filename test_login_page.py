from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


def test_login_url(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_login_login(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_login_reg(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()

