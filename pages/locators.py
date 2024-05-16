from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasketPageLocators:
    CONTINUE_SHOPPING_LINK = (By.CSS_SELECTOR, "#content_inner > p > a")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BTN_ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_NAME_ADD_PRODUCT = (By.CSS_SELECTOR,
                                "#messages > div:nth-child(1) > div > strong")
    MESSAGE_VALUE_BASKET = (By.CSS_SELECTOR, "#messages .alert-info strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
