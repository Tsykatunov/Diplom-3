from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class BrowserFactory:
    @staticmethod
    def get_browser(browser_name):
        if browser_name.lower() == "chrome":
            options = webdriver.ChromeOptions()
            service = ChromeService(ChromeDriverManager().install())
            return webdriver.Chrome(service=service, options=options)
        elif browser_name.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            service = FirefoxService(GeckoDriverManager().install())
            return webdriver.Firefox(service=service, options=options)
        else:
            raise ValueError(f"Browser {browser_name} is not supported") 