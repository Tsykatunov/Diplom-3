import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
import pytest

class TestPasswordRecovery:

    @pytest.fixture(autouse=True)
    def setup(self, driver, random_user, api_client):
        api_client.create_user(**random_user)
        self.email = random_user["email"]
        self.password = random_user["password"]

    @allure.title('Проверка перехода на страницу "забыл пароль"')
    def test_navigate_to_forgot_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open("/login")
        login_page.click_forgot_password_link()
        assert "forgot-password" in driver.current_url

    @allure.title('Проверка перехода на страницу "восстановления пароля"')
    def test_password_recovery(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.open("/forgot-password")
        forgot_page.set_email(self.email)
        forgot_page.click_recover_button()
        assert "reset-password" in driver.current_url

    @allure.title('Проверка переключения видимости пароля')
    def test_password_visibility_toggle(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_login_button()
        login_page = LoginPage(driver)
        login_page.click_forgot_password_link()
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.set_email("test@example.com")
        forgot_page.click_recover_button()
        reset_page = ResetPasswordPage(driver)
        new_password = "NewTestPassword123"
        reset_page.set_password(new_password)
        assert reset_page.get_password_input_type() == "password"
        reset_page.toggle_password_visibility()
        assert reset_page.get_password_input_type() == "text"
        reset_page.toggle_password_visibility()
        assert reset_page.get_password_input_type() == "password"