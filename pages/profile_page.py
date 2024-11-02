import allure
from .base_page import BasePage
from locators.locators import ProfilePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ProfilePage(BasePage):
    @allure.step("Нажатие кнопки выхода")
    def click_logout_button(self):
        logout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", logout_button)
        self.driver.implicitly_wait(1)
        self.driver.execute_script("arguments[0].click();", logout_button)

    @allure.step('Переход в историю заказов')
    def click_orders_history(self): 
        orders_history_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ProfilePageLocators.ORDERS_HISTORY)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", orders_history_button)
        try:
            modal = self.driver.find_element(By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
            if modal.is_displayed():
                modal.click()
                WebDriverWait(self.driver, 3).until(
                    EC.invisibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"))
                )
        except:
            pass
        self.driver.execute_script("arguments[0].click();", orders_history_button)
        
    @allure.step('Получение номера последнего заказа')
    def get_last_order_number(self):
        last_order_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ProfilePageLocators.LAST_ORDER_NUMBER)
        )
        return last_order_number.text.split('\n')[0].replace('#', '')