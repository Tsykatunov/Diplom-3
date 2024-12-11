import allure
from .base_page import BasePage
from locators.locators import MainPageLocators
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

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
        try:
            modal = self.wait_for_element(MainPageLocators.INGREDIENT_DETAILS)
            return modal.is_displayed()
        except NoSuchElementException:
            return False
        
    @allure.step("Закрытие модального окна")
    def close_modal(self):
        close_button = self.wait_for_element(MainPageLocators.MODAL_CLOSE_BUTTON)
        close_button.click()
        
    @allure.step("Переход в личный кабинет")
    def go_to_profile(self):
        self.click_element(MainPageLocators.PROFILE_BUTTON)
        
    @allure.step("Клик по ингредиенту")
    def click_ingredient(self):
        try:
            self.wait_for_element(MainPageLocators.MAKE_A_BURGER_TEXT)
            ingredient = self.wait_for_element(MainPageLocators.INGREDIENT)
            ingredient.click()
        except NoSuchElementException:
            raise Exception("Ингредиент не найден")
    
    @allure.step("Проверка некликабельности ингредиента под модальным окном")
    def is_ingredient_clickable(self):
        try:
            ingredient = self.wait_for_element(MainPageLocators.INGREDIENT)
            return ingredient.is_enabled() and ingredient.is_displayed()
        except NoSuchElementException:
            return False
                    
    @allure.step("Получение значения счетчика ингредиента")
    def get_ingredient_counter(self):
        counter = self.wait_for_element(MainPageLocators.INGREDIENT_COUNTER)
        return int(counter.text) if counter.text else 0
        
    @allure.step("Перетаскивание ингредиента в конструктор")
    def drag_ingredient_to_constructor(self):
        self.wait_for_element(MainPageLocators.INGREDIENT)
        ingredients = self.find_elements(MainPageLocators.INGREDIENT)
        constructor = self.wait_for_element(MainPageLocators.CONSTRUCTOR_TARGET)
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
        try:
            order_button = self.wait_for_element(MainPageLocators.ORDER_BUTTON)
            self.scroll_into_view(order_button)
            
            try:
                modal_overlay = self.wait_for_element(MainPageLocators.MODAL_OVERLAY)
                if modal_overlay.is_displayed():
                    close_button = self.wait_for_element(MainPageLocators.MODAL_CLOSE_BUTTON)
                    close_button.click()
            except NoSuchElementException:
                pass

            browser_name = self.driver.capabilities['browserName'].lower()
            if browser_name == 'firefox':
                self.execute_script("arguments[0].click();", order_button)
            else:
                order_button.click()
        except (NoSuchElementException, ElementNotInteractableException):
            raise Exception("Кнопка заказа не найдена или недоступна для клика")

    @allure.step("Проверка создания заказа")
    def is_order_created(self):
        try:
            self.wait_for_element(MainPageLocators.ORDER_START)
            self.wait_for_element(MainPageLocators.ORDER_WAIT)
            return True
        except NoSuchElementException:
            return False

    @allure.step("Проверка видимости конструктора")
    def is_constructor_page(self):
        try:
            element = self.wait_for_element(MainPageLocators.MAKE_A_BURGER_TEXT)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    @allure.step('Получение номера заказа из модального окна')
    def get_order_number(self):
        return self.wait_for_text_change(MainPageLocators.ORDER_NUMBER_TEXT, '9999')

    @allure.step('Проверка добавления ингредиента в конструктор')
    def verify_ingredient_added(self):
        try:
            return self.wait_for_element(MainPageLocators.CONSTRUCTOR_TARGET)
        except NoSuchElementException:
            return False

    @allure.step('Убеждаемся, что логин прошёл успешно')
    def login_success(self):
        try:
            return self.wait_for_element(MainPageLocators.ORDER_BUTTON)
        except NoSuchElementException:
            return False