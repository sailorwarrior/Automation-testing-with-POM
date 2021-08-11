from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_add_book_to_basket_correctly(self):
        self.book_name_in_basket_should_be_correct()
        self.book_cost_should_be_equal_to_basket_sum()

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def book_name_in_basket_should_be_correct(self):
        adding_book = self.browser.find_element(*ProductPageLocators.ADDING_BOOK_NAME)
        basket_book = self.browser.find_element(*ProductPageLocators.BOOK_IN_BASKET_NAME)
        adding_book_name = adding_book.text
        basket_book_name = basket_book.text
        assert adding_book_name == basket_book_name, "Book name in basket is not equual to added book name"

    def book_cost_should_be_equal_to_basket_sum(self):
        book_cost = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        basket_sum = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        book_cost_value = book_cost.text
        basket_sum_value = basket_sum.text
        assert book_cost_value == basket_sum_value, "Book cost and Basket sum doesnt match"
