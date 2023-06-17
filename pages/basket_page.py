from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        return self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY)

    def basket_has_no_products(self):
        return self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS)
