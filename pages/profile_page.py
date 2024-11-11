import allure
from .base_page import BasePage
from locators.locators import ProfilePageLocators, MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage(BasePage):
    @allure.step("Нажатие кнопки выхода")
    def click_logout_button(self):
        logout_button = self.wait_for_element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        self.scroll_into_view(logout_button)
        self.execute_script("arguments[0].click();", logout_button)

    @allure.step('Переход в историю заказов')
    def click_orders_history(self): 
        orders_history_button = self.wait_for_element_to_be_clickable(ProfilePageLocators.ORDERS_HISTORY)
        self.scroll_into_view(orders_history_button)
        modal = self.find_element(MainPageLocators.MODAL_OVERLAY)
        if modal.is_displayed():
            modal.click()
            self.wait_for_element_to_be_invisible(MainPageLocators.MODAL_OVERLAY)
        self.execute_script("arguments[0].click();", orders_history_button)
        
    @allure.step('Получение номера последнего заказа')
    def get_last_order_number(self):
        last_order_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ProfilePageLocators.LAST_ORDER_NUMBER)
        )
        return last_order_number.text.split('\n')[0].replace('#', '')