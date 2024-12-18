from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.locators import ResetPasswordPageLocators
from selenium.webdriver.common.action_chains import ActionChains
import allure

class ResetPasswordPage(BasePage):
    
    @allure.step('Ввод нового пароля')
    def set_password(self, password):
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ResetPasswordPageLocators.PASSWORD_INPUT)
        )
        password_input.clear()
        password_input.send_keys(password)

    @allure.step('Переключение видимости пароля')
    def toggle_password_visibility(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ResetPasswordPageLocators.PASSWORD_TOGGLE_BUTTON)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(button)
        actions.pause(1)
        actions.click()
        actions.perform()

    def get_password_input_type(self):
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ResetPasswordPageLocators.PASSWORD_INPUT)
        )
        return password_input.get_attribute('type')

    def get_password_value(self):
        password_input = self.find_element(ResetPasswordPageLocators.PASSWORD_INPUT)
        return password_input.get_attribute('value') 