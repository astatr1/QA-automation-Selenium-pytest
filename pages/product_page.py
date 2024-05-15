from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """Основная страница карточки товара"""
    def add_product_to_basket(self):
        """Добавление товара в корзину"""
        btn_add_to_basket = self.browser.find_element(
            *ProductPageLocators.BTN_ADD_PRODUCT_TO_BASKET)
        btn_add_to_basket.click()

    def should_be_message_to_add_product_to_basket(self):
        """Проверка соответствия добавляемого товара в корзину фактическому"""
        message_name_product_add_to_basket = self.browser.find_element(
            *ProductPageLocators.MESSAGE_NAME_ADD_PRODUCT).text

        name_product_add_to_basket = self.browser.find_element(
            *ProductPageLocators.NAME_PRODUCT).text

        assert (message_name_product_add_to_basket ==
                name_product_add_to_basket), \
            "Another product has been added to basket!"

    def should_be_message_about_value_of_the_basket(self):
        """Проверка соответствия значения стоимости товара в корзине
        фактической цене"""
        message_add_value_basket = self.browser.find_element(
            *ProductPageLocators.MESSAGE_VALUE_BASKET).text

        price_product = self.browser.find_element(
            *ProductPageLocators.PRICE_PRODUCT).text

        assert message_add_value_basket == price_product, \
            ("The cost of the product added to the basket "
             "is not equal to the price of the product!")

    def should_not_be_success_message(self):
        """Проверяем, что нет сообщения об успехе"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is present, but should not be"

    def should_be_disappeared_success_message(self):
        """Проверка, что нет исчезающего сообщения об успехе"""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is present, but should have disappeared"
