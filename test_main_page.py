from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


main_link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_do_to_login_page(browser):
    """Переход гостевого пользователя на страницу Логина"""
    page = MainPage(browser, main_link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """Проверка, что корзина пуста после перехода
    с главной страницы в корзину"""
    main_page = MainPage(browser, main_link)
    main_page.open()
    main_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_items_in_basket()
    basket_page.should_be_message_basket_empty()
    