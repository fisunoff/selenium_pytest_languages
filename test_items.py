link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"


def test_buy_btn(browser):
    browser.get(link)
    assert browser.find_element_by_css_selector("#add_to_basket_form > button"), "Кнопка не найдена"
