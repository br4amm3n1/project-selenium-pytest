from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_IS_EMPTY = (By.ID, "content_inner")
    BASKET_PRODUCTS = (By.CSS_SELECTOR, "h2.col-sm-6")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REG_FORM = (By.ID, "register_form")
    EMAIL_FIELD = (By.ID, "id_registration-email")
    PASSWORD_FIELD = (By.ID, "id_registration-password1")
    PASSWORD_CONFIRM_FIELD = (By.ID, "id_registration-password2")
    BUTTON_SUBMIT_REG = (By.NAME, "registration_submit")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    TITLE_IN_MESSAGE = (By.CSS_SELECTOR, "div.alertinner :first-child")
    TITLE_ADDED = (By.CSS_SELECTOR, "div.product_main h1")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "div.alertinner p strong")
    PRICE_ADDED = (By.CSS_SELECTOR, "div.product_main :nth-child(2)")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages :first-child :nth-child(2)")
