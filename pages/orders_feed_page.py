import allure
from .base_page import BasePage
from selenium.webdriver.common.by import By
from locators.locators import OrdersFeedPageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class OrdersFeedPage(BasePage):
    @allure.step("Проверка отображения текста 'Лента заказов'")
    def is_orders_feed_page(self):
        try:
            element = self.wait_for_element(OrdersFeedPageLocators.ORDERS_FEED_TEXT)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    @allure.step('Открытие страницы ленты заказов')
    def open_orders_feed(self):
        self.open("/feed")

    @allure.step('Клик по первому заказу в ленте')
    def click_first_order(self):
        try:
            first_order = self.wait_for_element(OrdersFeedPageLocators.FIRST_ORDER)
            if first_order.is_displayed() and first_order.is_enabled():
                first_order.click()
        except NoSuchElementException:
            raise Exception("Первый заказ не найден")
        
    @allure.step('Проверка отображения модального окна с деталями заказа')
    def is_order_details_modal_visible(self):
        try:
            modal = self.wait_for_element(OrdersFeedPageLocators.ORDER_DETAILS_MODAL)
            return modal.is_displayed()
        except NoSuchElementException:
            return False
        
    @allure.step('Проверка наличия заказа в ленте')
    def is_order_in_feed(self, order_number):
        try:
            locator = (OrdersFeedPageLocators.ORDER_BY_NUMBER[0], 
                    OrdersFeedPageLocators.ORDER_BY_NUMBER[1].format(order_number))
            order_element = self.wait_for_element(locator)
            return order_element.is_displayed()
        except NoSuchElementException:
            return False
    
    @allure.step('Получение количества заказов в ленте')
    def get_total_orders_count(self):
        try:
            total_orders_element = self.wait_for_element(OrdersFeedPageLocators.TOTAL_ORDERS_COUNT)
            return int(total_orders_element.text)
        except NoSuchElementException:
            return 0
    
    @allure.step('Получение количества заказов за сегодня')
    def get_today_orders_count(self):
        try:
            today_orders_element = self.wait_for_element(OrdersFeedPageLocators.TODAY_ORDERS_COUNT)
            return int(today_orders_element.text)
        except NoSuchElementException:
            return 0
    
    @allure.step('Проверка наличия заказа в разделе "В работе"')
    def is_order_in_progress(self, order_number):
        try:
            self.wait_for_element(OrdersFeedPageLocators.ORDERS_FEED_TEXT)
            order_elements = self.find_elements(OrdersFeedPageLocators.ORDER_NUMBERS)
            return any(order_number in order.text.strip() for order in order_elements)
        except NoSuchElementException:
            return False

    @allure.step('Закрытие модального окна заказа')
    def close_order_modal(self):
        body = self.wait_for_element((By.TAG_NAME, 'body'))
        body.send_keys(Keys.ESCAPE)