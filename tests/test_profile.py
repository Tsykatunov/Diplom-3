import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
import pytest

@pytest.mark.usefixtures("setup")
class TestProfile:
    @allure.title('Проверка перехода в личный кабинет')
    def test_profile_navigation(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_profile()
        assert "account/profile" in main_page.get_current_url()

    @allure.title('Проверка перехода в историю заказов')
    def test_orders_history_navigation(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_profile()
        profile_page = ProfilePage(driver)
        profile_page.click_orders_history()
        assert "account/order-history" in profile_page.get_current_url()

    @allure.title('Проверка выхода из аккаунта')
    def test_logout(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_profile()
        profile_page = ProfilePage(driver)
        profile_page.click_logout_button()
        assert profile_page.wait_for_url_change('login'), "Не произошел переход на страницу логина после выхода"