from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini span a")
    MAIN_LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    ITEMS_MARK = (By.CSS_SELECTOR, "h2.col-sm-6.h3")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    COST_MESSAGE = (By.CSS_SELECTOR,
                    "#messages > div:nth-child(3) > div > p > strong")
    PRODUCT_COST = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_MESSAGE = (By.CSS_SELECTOR,
                       "#messages > div > div strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div > div")


class LinksLocators:
    BASKET_LINK = "http://selenium1py.pythonanywhere.com/en-gb/basket/"
    FROM_PRODUCT_TO_LOGIN_LINK = ("http://selenium1py.pythonanywhere.com/"
                                  "en-gb/catalogue/the-city-and-the-stars_95/")
    LOGIN_LINK = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    MAIN_LINK = "http://selenium1py.pythonanywhere.com/"
    PRODUCT_LINK = ("http://selenium1py.pythonanywhere.com/"
                    "catalogue/the-shellcoders-handbook_209/?promo=newYear")
    PRODUCT_BASE_LINK = ("http://selenium1py.pythonanywhere.com/"
                         "catalogue/coders-at-work_207")
