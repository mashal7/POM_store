import time

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        self.is_element_present(ProductPageLocators.BUTTON_ADD)
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD).click()
        self.solve_quiz_and_get_code()
        self.should_be_product_in_basket()
        self.compare_name_of_book()
        self.compare_price_of_book()

    # Проверки
    def should_be_product_in_basket(self):
        text_for_checking = self.browser.find_element(*ProductPageLocators.MESSAGE).text
        assert 'has been added' in text_for_checking, 'Product has not been added in basket'
        print(f'Product has been added in basket')


    def should_not_be_success_message(self):
        assert self.is_not_element_present(ProductPageLocators.MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapeared_success_message(self):
        assert self.is_not_element_present(ProductPageLocators.MESSAGE), \
            "Success message is presented, but should not be"

    def compare_name_of_book(self):
        assert self.compare_text(ProductPageLocators.NAME_OF_BOOK, ProductPageLocators.NAME_OF_BOOK_IN_MESSAGE), 'Name of book in basket is not correct'
        print('Name of book in basket is correct')

    def compare_price_of_book(self):
        assert self.compare_text(ProductPageLocators.PRICE_OF_BOOK, ProductPageLocators.PRICE_OF_BOOK_IN_MESSAGE), 'Price of book in basket is not correct'
        print('Price of book in basket is correct')