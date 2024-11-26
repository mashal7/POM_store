from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text
        assert 'Your basket is empty' in text, 'Wrong! Basket is not empty'
        print('Basket is empty')

