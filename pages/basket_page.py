from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        self.should_be_no_items_in_the_cart()
        self.should_be_message()

    def should_be_no_items_in_the_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_MARK)

    def should_be_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE)
