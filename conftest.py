import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from utils.helpers import generate_timestamp, random_string, random_password
from utils.api_client import ApiClient
from pages.login_page import LoginPage
from locators.locators import MainPageLocators

@pytest.fixture
def random_user():
    timestamp = generate_timestamp()
    return {
        "email": f"test{timestamp}@tsykatunov.ru",
        "password": random_password(),
        "name": random_string()
    }

@pytest.fixture
def api_client():
    return ApiClient()

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browser = request.param
    driver = None

    try:
        if browser == 'chrome':
            options = Options()
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(options=options)
        elif browser == 'firefox':
            options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(options=options)

        driver.maximize_window()
        driver.implicitly_wait(10)

        yield driver

    finally:
        if driver is not None:
            driver.quit()

@pytest.fixture
def setup(driver, random_user, api_client):
    api_client.create_user(**random_user)
    driver.get("https://stellarburgers.nomoreparties.site/login")
    login_page = LoginPage(driver)
    login_page.set_email(random_user["email"])
    login_page.set_password(random_user["password"])
    login_page.click_login_button()
    for _ in range(10):
        if driver.find_elements(*MainPageLocators.ORDER_BUTTON):
            return
    raise Exception("Не удалось выполнить вход в систему, кнопка заказа не найдена.")