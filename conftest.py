import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.main_page import MainPage
from utils.helpers import generate_timestamp, random_string, random_password, generate_random_user
from utils.api_client import ApiClient
from pages.login_page import LoginPage

@pytest.fixture
def random_user():
    return generate_random_user()

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
    login_page = LoginPage(driver)
    login_page.open("/login")
    main_page = MainPage(driver)
    login_page.set_email(random_user["email"])
    login_page.set_password(random_user["password"])
    login_page.click_login_button()
    main_page.login_success()
