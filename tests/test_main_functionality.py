import allure
import pytest
from pages.main_page import MainPage
from pages.orders_feed_page import OrdersFeedPage
class TestMainFunctionality:

    @allure.title('Проверка перехода в конструктор')
    def test_constructor_navigation(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_orders_feed()
        main_page.go_to_constructor()
        assert main_page.is_constructor_page()
    
    @allure.title('Проверка перехода в Ленту заказов')
    def test_orders_feed_navigation(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_orders_feed()
        orders_feed_page = OrdersFeedPage(driver)
        assert orders_feed_page.is_orders_feed_page()

    @allure.title('Проверка открытия модального окна ингредиента')
    def test_ingredient_modal_open(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient()
        assert main_page.is_modal_visible()
        
    @allure.title('Проверка закрытия модального окна ингредиента')
    def test_ingredient_modal_close(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient()
        main_page.close_modal()
        assert main_page.is_ingredient_clickable()

    @allure.title('Проверка счетчика ингредиентов')
    def test_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        initial_count = main_page.get_ingredient_counter()
        main_page.drag_ingredient_to_constructor()
        
        assert main_page.verify_ingredient_added() is not None
        
        new_count = main_page.get_ingredient_counter()
        assert new_count > initial_count

    @allure.title('Проверка оформления заказа')
    def test_place_order(self, driver, setup):
        main_page = MainPage(driver)
        main_page.open()
        main_page.drag_ingredient_to_constructor()
        main_page.click_order_button()        
        assert main_page.is_order_created()