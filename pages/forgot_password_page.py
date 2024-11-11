from .base_page import BasePage
from locators.locators import ForgotPasswordPageLocators
import allure

class ForgotPasswordPage(BasePage):
    
    @allure.step('Ввод email для восстановления')
    def set_email(self, email):
        self.enter_text(ForgotPasswordPageLocators.EMAIL_INPUT, email)

    @allure.step('Клик по кнопке восстановления')
    def click_recover_button(self):
        self.click_element(ForgotPasswordPageLocators.RECOVER_BUTTON)
