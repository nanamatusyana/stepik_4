from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
class LoginPageLocators:
    LOGIN_FORM=(By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM=(By.CSS_SELECTOR, "#register_form")
    USER_EMAIL_FORM = (By.CSS_SELECTOR, "#id_login-username")
    USER_PASSWORD_FORM= (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BTN=(By.CSS_SELECTOR, ".btn-lg")
    GUEST_EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    GUEST_PASSWORD_FORM1 = (By.CSS_SELECTOR,  "[name='registration-password1']")
    GUEST_PASSWORD_FORM2 = (By.CSS_SELECTOR, "[name='registration-password2']")
    REG_BTN = (By.CSS_SELECTOR, "[name='registration_submit']")
class ProductPageLocators:
    ADD_TO_CART=(By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME=(By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")
    PRODUCT_PRICE=(By.CSS_SELECTOR, ".price_color")
    ALERT_PRODUCT_NAME=(By.CSS_SELECTOR,"div.alertinner>strong")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR,".alert-success")
class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class BasketPageLocators:
    VIEW_CART_BTN = (By.CSS_SELECTOR, "div.basket-mini span.btn-group a.btn.btn-default")
    EMPTY_CART=(By.CSS_SELECTOR, "#content_inner p")
    ITEMS_IN_CART=(By.CSS_SELECTOR, ".basket-items")