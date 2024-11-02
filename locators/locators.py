from selenium.webdriver.common.by import By

class MainPageLocators:
    PROFILE_BUTTON = (By.XPATH, "//a[@href='/account']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    ORDERS_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    MAKE_A_BURGER_TEXT = (By.XPATH, "//h1[text()='Соберите бургер']")
    INGREDIENT = (By.CSS_SELECTOR, "[class^='BurgerIngredient_ingredient__']")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "[class^='counter_counter__']")
    CONSTRUCTOR_TARGET = (By.CSS_SELECTOR, "[class^='BurgerConstructor_basket__']")
    INGREDIENT_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button.Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_START = (By.XPATH, "//*[text()='Ваш заказ начали готовить']")
    ORDER_WAIT = (By.XPATH, "//*[text()='Дождитесь готовности на орбитальной станции']")
    ORDER_NUMBER_TEXT = (By.CSS_SELECTOR, "h2[class*='Modal_modal__title']")

class ProfilePageLocators:
    ORDERS_HISTORY = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    LAST_ORDER_NUMBER = (By.CSS_SELECTOR, "ul[class*='OrderHistory_profileList'] li:last-child")

class LoginPageLocators:
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")

class ForgotPasswordPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='text']")
    RECOVER_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")

class ResetPasswordPageLocators:
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input.text.input__textfield.text_type_main-default")
    PASSWORD_TOGGLE_BUTTON = (By.CSS_SELECTOR, "div.input__icon.input__icon-action svg")
    
class OrdersFeedPageLocators:
    ORDERS_FEED_TEXT = (By.XPATH, "//h1[text()='Лента заказов']")
    FIRST_ORDER = (By.XPATH, "(//li[contains(@class, 'OrderHistory_listItem')])[1]")
    TOTAL_ORDERS_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'text_type_digits-large')]")
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'text_type_digits-large')]")
    ORDER_NUMBERS = (By.CSS_SELECTOR, "li.text.text_type_digits-default.mb-2")
    ORDER_DETAILS_MODAL = (By.CSS_SELECTOR, "p.text.text_type_main-medium.mb-8")