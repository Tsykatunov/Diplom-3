from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site"
        
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        
    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        
    def click_element(self, locator, timeout=10):
        try:
            element = self.wait_for_element_to_be_clickable(locator, timeout)
            element.click()
        except ElementClickInterceptedException:
            self._handle_modals()
            element = self.wait_for_element_to_be_clickable(locator, timeout)
            element.click()
        return element
        
    def enter_text(self, locator, text, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(text)
        return element
        
    def open(self, path=""):
        retries = 3
        while retries > 0:
            try:
                self.driver.get(f"{self.base_url}{path}")
                WebDriverWait(self.driver, 20).until(
                    lambda driver: driver.execute_script('return document.readyState') == 'complete'
                )
                self._handle_modals()
                return
            except:
                retries -= 1
                if retries == 0:
                    raise
                
    def _handle_modals(self):
        try:
            modals = self.driver.find_elements(*MainPageLocators.MODAL_OVERLAY)
            for modal in modals:
                if modal.is_displayed():
                    close_button = modal.find_element(*MainPageLocators.MODAL_CLOSE_BUTTON)
                    close_button.click()
                    WebDriverWait(self.driver, 3).until(
                        EC.invisibility_of_element_located(*MainPageLocators.MODAL_OVERLAY)
                    )
        except NoSuchElementException:
            print("No modals found on the page.")


    def is_element_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return True

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def scroll_into_view(self, element):
        self.execute_script("arguments[0].scrollIntoView(true);", element)

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_to_be_invisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )