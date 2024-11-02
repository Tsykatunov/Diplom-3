import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from datetime import datetime
import random
import string
from utils.api_client import ApiClient

def generate_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S_%f")

def random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def random_password(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

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
def logged_in_driver(driver, random_user, api_client):
    api_client.create_user(**random_user)
    driver.get("https://stellarburgers.nomoreparties.site/login")
    login_page = LoginPage(driver)
    login_page.login(random_user["email"], random_user["password"])
    
    return driver