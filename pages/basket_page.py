from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    """Страница корзины товара"""
    def should_be_message_basket_empty(self):
        """Есть сообщение, что корзина пуста"""
        assert self.is_element_present(
            *BasketPageLocators.CONTINUE_SHOPPING_LINK), \
            "Должна быть ссылка продолжения покупок в пустой корзине!"

    def should_be_no_items_in_basket(self):
        """В корзине нет элементов с товарами"""
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "В корзине не должно быть товаров"
