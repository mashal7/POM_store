from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group a.btn.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL = (By.CSS_SELECTOR, '[name="registration-email"]')
    PASSWORD = (By.CSS_SELECTOR, '[name="registration-password1"]')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '[name="registration-password2"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')

class ProductPageLocators:
    BUTTON_ADD = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    MESSAGE =(By.CSS_SELECTOR, '#messages :first-child.alert .alertinner')
    NAME_OF_BOOK_IN_MESSAGE = (By.CSS_SELECTOR, '#messages :first-child.alert .alertinner strong')
    NAME_OF_BOOK = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    PRICE_OF_BOOK_IN_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(3).alert .alertinner strong')
    PRICE_OF_BOOK = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')

class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner p')