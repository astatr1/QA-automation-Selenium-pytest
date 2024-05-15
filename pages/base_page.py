import math
from selenium.common.exceptions import NoSuchElementException, \
    NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        """Переход на страницу Логина"""
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        """Проверка наличия кнопки Логина"""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            "Login link is not presented"

    def open(self):
        """Открытие страницы"""
        self.browser.get(self.url)

    def is_element_present(self, method, css_selector):
        """Проверка наличия элемента"""
        try:
            self.browser.find_element(method, css_selector)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, method, css_selector, timeout=4):
        """Проверка отсутствия элемента"""
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((method, css_selector)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, method, css_selector, timeout=4):
        """Проверка исчезновения элемента"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
             until_not(EC.presence_of_element_located((method, css_selector)))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        """Решение задачи и получение кода"""
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Ваш код: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("Не получено второе уведомление браузера с кодом!")
