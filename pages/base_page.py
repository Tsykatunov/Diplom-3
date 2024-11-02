from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site"
        
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        
    def click_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        try:
            modal = self.driver.find_element(By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
            if modal.is_displayed():
                modal.click()
                WebDriverWait(self.driver, 3).until(
                    EC.invisibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"))
                )
        except:
            pass

        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)
        
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
            modals = self.driver.find_elements(By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
            for modal in modals:
                if modal.is_displayed():
                    close_button = modal.find_element(By.CLASS_NAME, "Modal_modal__close__TnseK")
                    close_button.click()
                    WebDriverWait(self.driver, 3).until(
                        EC.invisibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"))
                    )
        except:
            pass

    def is_element_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return True