import allure
from .base_page import BasePage
from locators.locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    @allure.step('Ввод email')
    def set_email(self, email):
        email_input = WebDriverWait(self.driver, 15).until(  # Увеличиваем время ожидания
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        email_input.clear()
        email_input.send_keys(email)

    @allure.step('Ввод пароля')
    def set_password(self, password):
        password_input = WebDriverWait(self.driver, 15).until(  # Увеличиваем время ожидания
            EC.presence_of_element_located(LoginPageLocators.PASSWORD_INPUT)
        )
        password_input.clear()
        password_input.send_keys(password)

    @allure.step('Клик по кнопке входа')
    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Клик по ссылке восстановления пароля')
    def click_forgot_password_link(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK) 