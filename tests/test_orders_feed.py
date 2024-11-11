import allure
import pytest
from pages.orders_feed_page import OrdersFeedPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage

@allure.feature('Лента заказов')
class TestOrdersFeed:
    @pytest.mark.usefixtures("setup")
    @allure.title('Проверка открытия деталей заказа')
    def test_order_details(self, driver):
        orders_page = OrdersFeedPage(driver)
        orders_page.open_orders_feed()
        orders_page.click_first_order()
        assert orders_page.is_order_details_modal_visible()

    @pytest.mark.usefixtures("setup")
    @allure.title('Проверка отображения заказа в общей ленте')
    def test_orders_history_display(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.drag_ingredient_to_constructor()
        main_page.click_order_button()
        orders_page = OrdersFeedPage(driver)
        orders_page.close_order_modal()
        main_page.go_to_profile()
        profile_page = ProfilePage(driver)
        profile_page.click_orders_history()
        order_number = profile_page.get_last_order_number()
        assert order_number is not None
        
    @pytest.mark.usefixtures("setup")
    @allure.title('Проверка увеличения счетчика выполненных заказов')
    def test_total_orders_counter(self, driver):
        orders_page = OrdersFeedPage(driver)
        orders_page.open_orders_feed()
        initial_total = orders_page.get_total_orders_count()
        main_page = MainPage(driver)
        main_page.open()
        main_page.drag_ingredient_to_constructor()
        main_page.click_order_button()
        orders_page.open_orders_feed()
        new_total = orders_page.get_total_orders_count()
        assert new_total > initial_total
        
    @pytest.mark.usefixtures("setup")
    @allure.title('Проверка увеличения счетчика заказов за сегодня')
    def test_today_orders_counter(self, driver):
        orders_page = OrdersFeedPage(driver)
        orders_page.open_orders_feed()
        initial_total = orders_page.get_today_orders_count()
        main_page = MainPage(driver)
        main_page.open()
        main_page.drag_ingredient_to_constructor()
        main_page.click_order_button()
        orders_page.open_orders_feed()
        new_total = orders_page.get_today_orders_count()
        assert new_total > initial_total
        
    @pytest.mark.usefixtures("setup")
    @allure.title('Проверка появления заказа в разделе "В работе"')
    def test_order_in_progress(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.drag_ingredient_to_constructor()
        main_page.click_order_button()
        order_number = main_page.get_order_number()        
        orders_page = OrdersFeedPage(driver)
        orders_page.close_order_modal()
        orders_page.open_orders_feed()
        assert orders_page.is_order_in_progress(order_number)