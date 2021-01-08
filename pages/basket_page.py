from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def go_to_basket(self):
        basket_btn = self.browser.find_element(*BasketPageLocators.VIEW_CART_BTN)
        basket_btn.click()
    def should_be_empty_basket_massege(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_CART), "Cart is not empty"
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_CART), "There is some items in cart"
