from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
class LoginPageLocators:
    LOGIN_FORM=(By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM=(By.CSS_SELECTOR, "#register_form")
class ProductPageLocators:
    ADD_TO_CART=(By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME=(By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")
    PRODUCT_PRICE=(By.CSS_SELECTOR, ".price_color")
    ALERT_PRODUCT_NAME=(By.CSS_SELECTOR,"div.alertinner>strong")