from .base_page import BasePage
from locators.locators import ForgotPasswordPageLocators
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ForgotPasswordPage(BasePage):
    
    @allure.step('Ввод email для восстановления')
    def set_email(self, email):
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ForgotPasswordPageLocators.EMAIL_INPUT)
        )
        email_input.clear()
        email_input.send_keys(email)

    @allure.step('Клик по кнопке восстановления')
    def click_recover_button(self):
        self.click_element(ForgotPasswordPageLocators.RECOVER_BUTTON)
