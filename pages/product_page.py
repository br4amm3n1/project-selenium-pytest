from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    # метод проверки существования кнопки "Добавить в корзину"
    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET)

    # метод сравнения названий книги в сообщении и на странице покупки
    def should_be_title_added_equals_title_in_message(self):
        text_title_in_message = self.browser.find_element(*ProductPageLocators.TITLE_IN_MESSAGE).text
        text_title_book_added = self.browser.find_element(*ProductPageLocators.TITLE_ADDED).text

        assert text_title_book_added == text_title_in_message, "Book titles are different."

    # метод сравнения цен книги в сообщении и на странице покупки
    def should_be_price_added_equals_price_in_message(self):
        text_price_in_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        text_price_added = self.browser.find_element(*ProductPageLocators.PRICE_ADDED).text

        assert text_price_added == text_price_in_message, "Prices aren't equal"

    # метод проверки отсутствия блока сообщений об успешном добавлении товара в корзину
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    # метод нажатия кнопки "Добавить в корзину"
    def add_in_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_button.click()
