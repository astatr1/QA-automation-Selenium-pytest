from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """Страница авторизации пользователя или регистрации"""
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверка наличия кнопки Логина"""
        assert "login" in self.browser.current_url, "'login' not found in URL"

    def should_be_login_form(self):
        """Проверка наличия формы Логина"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not present"

    def should_be_register_form(self):
        """Проверка наличия формы регистрации пользователя"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not present"

    def register_new_user(self, email, password):
        """Регистрация нового пользователя"""
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)

        password_field_1 = self.browser.find_element(
            *LoginPageLocators.PASSWORD_FIELD_1)
        password_field_1.send_keys(password)

        password_field_2 = self.browser.find_element(
            *LoginPageLocators.PASSWORD_FIELD_2)
        password_field_2.send_keys(password)

        btn_register_submit = self.browser.find_element(
            *LoginPageLocators.BTN_REGISTER_SUBMIT)
        btn_register_submit.click()
