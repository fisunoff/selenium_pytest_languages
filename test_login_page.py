from .pages.locators import LinksLocators
from .pages.login_page import LoginPage


def test_should_be_login_page(browser):
    login_page = LoginPage(browser, LinksLocators.LOGIN_LINK)
    login_page.open()
    login_page.should_be_login_page()
