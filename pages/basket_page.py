from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY) and \
               self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS), \
               "Basket isn't empty"
