from pages.product_page import ProductPage
import pytest


base_url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'


@pytest.mark.parametrize('link', [f"{base_url}{i}" for i in range(10)])
def test_guest_can_add_product_to_basket(browser, link):
    if link == f"{base_url}7":
        pytest.xfail(f"Skipping test for link: {link}")
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_to_add_product_to_basket()
    page.should_be_message_about_value_of_the_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = ("http://selenium1py.pythonanywhere.com/"
            "catalogue/the-city-and-the-stars_95/")
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_to_login_page_from_product_page(browser):
    link = ("http://selenium1py.pythonanywhere.com/"
            "catalogue/the-city-and-the-stars_95/")
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
