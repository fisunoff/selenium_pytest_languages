from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.add_product()
        self.solve_quiz_and_get_code()
        self.should_be_correct_product()
        self.should_be_correct_cost()

    def add_product(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def should_be_correct_product(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)

        product_in_basket = self.browser.find_element(*ProductPageLocators.
                                                      PRODUCT_MESSAGE)

        assert product.text == product_in_basket.text, (
            f"Wrong item in the cart. Should be '{product.text}',"
            f"but given '{product_in_basket.text}'.")

    def should_be_correct_cost(self):
        product_cost = ((self.browser.find_element(
            *ProductPageLocators.PRODUCT_COST))
            .text).translate(str.maketrans(
             "", "", "£  "))

        cost_in_basket = ((self.browser.find_element(
            *ProductPageLocators.COST_MESSAGE))
            .text).translate(str.maketrans(
             "", "", "£  "))

        assert product_cost == cost_in_basket, (
            f"Wrong cost. Should be {product_cost}, "
            f"but given {cost_in_basket}.")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), (
            "Success message is presented")

    def message_should_disappear(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), (
            "The message did not disappear")
