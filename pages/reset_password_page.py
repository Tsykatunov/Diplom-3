from .base_page import BasePage
from locators.locators import ResetPasswordPageLocators
from selenium.webdriver.common.action_chains import ActionChains
import allure

class ResetPasswordPage(BasePage):
    
    @allure.step('Ввод нового пароля')
    def set_password(self, password):
        password_input = self.wait_for_element(ResetPasswordPageLocators.PASSWORD_INPUT)
        if password_input.get_attribute('type') != 'password':
            self.click_element(ResetPasswordPageLocators.PASSWORD_VISIBILITY_TOGGLE)
        self.enter_text(ResetPasswordPageLocators.PASSWORD_INPUT, password)

    @allure.step('Переключение видимости пароля')
    def toggle_password_visibility(self):
        button = self.wait_for_element(ResetPasswordPageLocators.PASSWORD_TOGGLE_BUTTON)
        actions = ActionChains(self.driver)
        actions.move_to_element(button)
        actions.pause(1)
        actions.click()
        actions.perform()

    def get_password_input_type(self):
        password_input = self.wait_for_element(ResetPasswordPageLocators.PASSWORD_INPUT)
        return password_input.get_attribute('type')

    def get_password_value(self):
        password_input = self.wait_for_element(ResetPasswordPageLocators.PASSWORD_INPUT)
        return password_input.get_attribute('value') 