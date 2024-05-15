from pages.product_page import ProductPage
import pytest


base_url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
product_link = ("http://selenium1py.pythonanywhere.com/"
            "catalogue/the-city-and-the-stars_95/")


@pytest.mark.parametrize('link', [f"{base_url}{i}" for i in range(10)])
def test_guest_can_add_promo_product_to_basket(browser, link):
    """Добавление гостевым пользователем промо товара в корзину"""
    if link == f"{base_url}7":
        pytest.xfail(f"Skipping test for link: {link}")
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_to_add_product_to_basket()
    page.should_be_message_about_value_of_the_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    """Наличие кнопки Логина у гостевого пользователя на странице товара"""
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()


def test_guest_can_to_login_page_from_product_page(browser):
    """Переход гостевого пользователя со страницы товара в Логин"""
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_login_page()

@pytest.mark.xfail(reason="Negative test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Негативный тест. Отсутствие сообщение
    об успешном добавлении товара в корзину"""
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    """Отсутствие сообщения об успехе"""
    page = ProductPage(browser, product_link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="Negative test")
def test_message_disappeared_after_adding_product_to_basket(browser):
    """Отсутствует исчезающее сообщение об успехе"""
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_basket()
    page.should_be_disappeared_success_message()
