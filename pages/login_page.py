import allure
from .base_page import BasePage
from locators.locators import LoginPageLocators
from selenium.common.exceptions import ElementClickInterceptedException

class LoginPage(BasePage):
    @allure.step('Ввод email')
    def set_email(self, email):
        email_input = self.wait_for_element(LoginPageLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)

    @allure.step('Ввод пароля')
    def set_password(self, password):
        password_input = self.wait_for_element(LoginPageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

    @allure.step('Клик по кнопке входа')
    def click_login_button(self):
        login_button = self.wait_for_element(LoginPageLocators.LOGIN_BUTTON)
        try:
            login_button.click()
        except ElementClickInterceptedException:
            self.execute_script("arguments[0].click();", login_button)

    @allure.step('Клик по ссылке восстановления пароля')
    def click_forgot_password_link(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK) 