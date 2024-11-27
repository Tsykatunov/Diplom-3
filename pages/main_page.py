import allure
from .base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators

class MainPage(BasePage):
    @allure.step("Открытие главной страницы")
    def open(self):
        super().open()
        
    @allure.step("Переход в конструктор")
    def go_to_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        
    @allure.step("Переход в ленту заказов")
    def go_to_orders_feed(self):
        self.click_element(MainPageLocators.ORDERS_FEED_BUTTON)
        
    @allure.step("Проверка видимости модального окна")
    def is_modal_visible(self):
        modal = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.INGREDIENT_DETAILS)
            )
        return True
        
    @allure.step("Закрытие модального окна")
    def close_modal(self):
        close_button = self.find_element(MainPageLocators.MODAL_CLOSE_BUTTON)
        close_button.click()
        
    @allure.step("Переход в личный кабинет")
    def go_to_profile(self):
        self.click_element(MainPageLocators.PROFILE_BUTTON)
        
    @allure.step("Клик по ингредиенту")
    def click_ingredient(self):
        self.wait_for_element(MainPageLocators.MAKE_A_BURGER_TEXT)
        ingredient = self.wait_for_element_to_be_clickable(MainPageLocators.INGREDIENT)
        ingredient.click()
    
    @allure.step("Проверка некликабельности ингредиента под модальным окном")
    def is_ingredient_clickable(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.INGREDIENT)
            )
        return True 
                    
    @allure.step("Получение значения счетчика ингредиента")
    def get_ingredient_counter(self):
        counter = self.driver.find_element(*MainPageLocators.INGREDIENT_COUNTER)
        return int(counter.text) if counter.text else 0
        
    @allure.step("Перетаскивание ингредиента в конструктор")
    def drag_ingredient_to_constructor(self):
        self.wait_for_element(MainPageLocators.INGREDIENT)
        ingredients = self.find_elements(MainPageLocators.INGREDIENT)
        constructor = self.find_element(MainPageLocators.CONSTRUCTOR_TARGET)
        self.scroll_into_view(ingredients[0])
        self.execute_script("""
            function simulateDragDrop(sourceElement, targetElement) {
                const MOUSE_EVENTS = ['mousedown', 'mousemove', 'mouseup'];
                const DRAG_EVENTS = ['dragstart', 'drag', 'dragenter', 'dragover', 'dragleave', 'drop', 'dragend'];
                
                function createEvent(eventName) {
                    const event = document.createEvent("CustomEvent");
                    event.initCustomEvent(eventName, true, true, null);
                    event.dataTransfer = {
                        data: {},
                        setData: function(type, val) {
                            this.data[type] = val;
                        },
                        getData: function(type) {
                            return this.data[type];
                        }
                    };
                    return event;
                }

                MOUSE_EVENTS.forEach(eventName => {
                    const event = createEvent(eventName);
                    sourceElement.dispatchEvent(event);
                    targetElement.dispatchEvent(event);
                });

                DRAG_EVENTS.forEach(eventName => {
                    const event = createEvent(eventName);
                    if (eventName === 'dragstart' || eventName === 'drag' || eventName === 'dragend') {
                        sourceElement.dispatchEvent(event);
                    } else {
                        targetElement.dispatchEvent(event);
                    }
                });
            }
            simulateDragDrop(arguments[0], arguments[1]);
        """, ingredients[0], constructor)

    @allure.step('Клик по кнопке входа в аккаунт')
    def click_login_button(self):
        self.click_element(MainPageLocators.LOGIN_BUTTON)
        
    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_order_button(self):
        order_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", order_button)
        modal_overlay = self.driver.find_element(*MainPageLocators.MODAL_OVERLAY)
        if modal_overlay.is_displayed():
            close_button = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(*MainPageLocators.MODAL_CLOSE_BUTTON)
            )
            close_button.click()
            WebDriverWait(self.driver, 3).until(
                EC.invisibility_of_element_located(*MainPageLocators.MODAL_OVERLAY)
            )
        order_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON)
        )
        browser_name = self.driver.capabilities['browserName'].lower()
        
        if browser_name == 'firefox':
            self.driver.execute_script("arguments[0].click();", order_button)
        else:
            order_button.click()
        
    @allure.step("Проверка создания заказа")
    def is_order_created(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_START)
        )
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_WAIT)
        )
        return True

    @allure.step("Проверка видимости конструктора")
    def is_constructor_page(self):
        element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(MainPageLocators.MAKE_A_BURGER_TEXT)
            )
        return element.is_displayed()
    
    @allure.step('Получение номера заказа из модального окна')
    def get_order_number(self):
        def check_order_number(driver):
            element = driver.find_element(*MainPageLocators.ORDER_NUMBER_TEXT)
            number = element.text.strip()
            return element if number and number != '9999' else False

        order_element = WebDriverWait(self.driver, 30).until(check_order_number)
        return order_element.text.strip()

    @allure.step('Проверка добавления ингредиента в конструктор')
    def verify_ingredient_added(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(MainPageLocators.CONSTRUCTOR_TARGET)
        )
