from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.
                                                REGISTER_EMAIL)
        email_field.send_keys(email)

        password_field = self.browser.find_element(*LoginPageLocators.
                                                   REGISTER_PASSWORD)
        password_field.send_keys(password)

        password_confirm_field = self.browser.find_element(
            *LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        password_confirm_field.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.
                                                    REGISTER_BUTTON)
        register_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url_string = self.url
        login = url_string.find("login")
        assert login != -1, "Incorrect url. This is not a login page."

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), (
            "There is no login form. This is not a login page.")

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), (
            "There is no registration form. This is not a login page.")
