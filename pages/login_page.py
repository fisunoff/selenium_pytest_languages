from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "That's not login page!"

    def should_be_login_form(self):
        assert (self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL) and self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)), "Incorrect login form"

    def should_be_register_form(self):
        assert (self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL) and
                self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD) and
                self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)), "Incorrect login form"
