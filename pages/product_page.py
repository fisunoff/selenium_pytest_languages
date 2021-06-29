from .base_page import BasePage
from .locators import ProductPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def buy_btn(self):
        link = self.browser.find_element(*ProductPageLocators.BUY_BTN)
        link.click()
        self.solve_quiz_and_get_code()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        msg_book_name = self.browser.find_element(*ProductPageLocators.MSG_BOOK_NAME).text
        assert book_name == msg_book_name, "Names don't match"
