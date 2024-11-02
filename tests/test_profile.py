import allure
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
import pytest

class TestProfile:

    @pytest.fixture(autouse=True)
    def setup(self, driver, random_user, api_client):
        api_client.create_user(**random_user)
        driver.get("https://stellarburgers.nomoreparties.site/login")
        login_page = LoginPage(driver)
        login_page.set_email(random_user["email"])
        login_page.set_password(random_user["password"])
        login_page.click_login_button()
        WebDriverWait(driver, 5).until(
            lambda x: "login" not in x.current_url
        )

    @allure.title('Проверка перехода в личный кабинет')
    def test_profile_navigation(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_profile()
        WebDriverWait(driver, 5).until(
            lambda x: "account/profile" in x.current_url
        )
        assert "account/profile" in driver.current_url

    @allure.title('Проверка перехода в историю заказов')
    def test_orders_history_navigation(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_profile()
        WebDriverWait(driver, 5).until(
            lambda x: "account/profile" in x.current_url
        )
        profile_page = ProfilePage(driver)
        profile_page.click_orders_history()
        WebDriverWait(driver, 5).until(
            lambda x: "account/order-history" in x.current_url
        )
        assert "account/order-history" in driver.current_url
    @allure.title('Проверка выхода из аккаунта')
    def test_logout(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_profile()
        WebDriverWait(driver, 5).until(
            lambda x: "account/profile" in x.current_url
        )
        profile_page = ProfilePage(driver)
        profile_page.click_logout_button()
        WebDriverWait(driver, 5).until(
            lambda x: "login" in x.current_url
        )
        assert "login" in driver.current_url