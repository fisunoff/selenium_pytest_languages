import pytest
from mimesis import Person

from .pages.basket_page import BasketPage
from .pages.locators import LinksLocators
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

person = Person()


urls = ([pytest.param(f"{LinksLocators.PRODUCT_BASE_LINK}/"
                      f"?promo=offer{number}",
        marks=pytest.mark.xfail(number == 7,
                                reason="expected bug for example"))
        for number in range(10)])


@pytest.mark.need_review
@pytest.mark.parametrize("link", urls)
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()



@pytest.mark.xfail(reason="Negative check")
def test_guest_cant_see_success_message_after_adding_product_to_basket(
        browser):
    product_page = ProductPage(browser, LinksLocators.PRODUCT_LINK)
    product_page.open()
    product_page.add_product()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, LinksLocators.PRODUCT_LINK)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason="Negative check")
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, LinksLocators.PRODUCT_LINK)
    product_page.open()
    product_page.add_product()
    product_page.solve_quiz_and_get_code()
    product_page.message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, LinksLocators.FROM_PRODUCT_TO_LOGIN_LINK)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, LinksLocators.FROM_PRODUCT_TO_LOGIN_LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, LinksLocators.FROM_PRODUCT_TO_LOGIN_LINK)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, LinksLocators.BASKET_LINK)
    basket_page.should_be_basket_empty()


@pytest.mark.user_logged_in
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = person.email(unique=True)
        password = person.password(length=10)
        login_page = LoginPage(browser, LinksLocators.LOGIN_LINK)
        login_page.open()
        login_page.register_new_user(email, password)

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, LinksLocators.PRODUCT_LINK)
        product_page.open()
        product_page.should_be_authorized_user()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, LinksLocators.PRODUCT_LINK)
        product_page.open()
        product_page.should_be_authorized_user()
        product_page.add_product_to_basket()
