import allure
from .base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators.locators import OrdersFeedPageLocators, MainPageLocators

class OrdersFeedPage(BasePage):
    @allure.step("Проверка отображения текста 'Лента заказов'")
    def is_orders_feed_page(self):
        return self.is_element_visible(OrdersFeedPageLocators.ORDERS_FEED_TEXT)

    @allure.step('Открытие страницы ленты заказов')
    def open_orders_feed(self):
        self.driver.get(f"{self.base_url}/feed")

    @allure.step('Клик по первому заказу в ленте')
    def click_first_order(self):
        first_order = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrdersFeedPageLocators.FIRST_ORDER)
        )
        first_order.click()
        
    @allure.step('Проверка отображения модального окна с деталями заказа')
    def is_order_details_modal_visible(self):
        WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(OrdersFeedPageLocators.ORDER_DETAILS_MODAL)
            )
        return True
        
    @allure.step("Закрытие модального окна")
    def close_order_modal(self):
        WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(MainPageLocators.ORDER_START)
            )
        WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(MainPageLocators.ORDER_WAIT)
            )
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(MainPageLocators.ORDER_START)
        )
        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(MainPageLocators.ORDER_WAIT)
        )

    @allure.step('Проверка наличия заказа в ленте')
    def is_order_in_feed(self, order_number):
        order_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, f"//*[contains(text(), '{order_number}')]")
                )
            )
        print(f"Found order: {order_element.text}")
        return True
    
    @allure.step('Получение количества заказов в ленте')
    def get_total_orders_count(self):
        total_orders_element = self.find_element(OrdersFeedPageLocators.TOTAL_ORDERS_COUNT)
        return int(total_orders_element.text)
    
    @allure.step('Получение количества заказов за сегодня')
    def get_today_orders_count(self):
        today_orders_element = self.find_element(OrdersFeedPageLocators.TODAY_ORDERS_COUNT)
        return int(today_orders_element.text)
    
    @allure.step('Проверка наличия заказа в разделе "В работе"')
    def is_order_in_progress(self, order_number):
        self.find_element(OrdersFeedPageLocators.ORDERS_FEED_TEXT)
        order_elements = self.driver.find_elements(*OrdersFeedPageLocators.ORDER_NUMBERS)
        return any(order_number in order.text.strip() for order in order_elements)