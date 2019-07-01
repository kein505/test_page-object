from .base_page import BasePage
from .locators import BasePageLocators


class CartPage(BasePage):
    def should_not_be_product_in_cart(self):
        self.should_be_basket_url()
        self.should_not_be_items_in_basket()
        self.should_not_be_product_in_basket()
        self.should_not_be_product_in_cart_message()
        self.should_not_be_product_in_cart_selector()

    def should_be_basket_url(self):
        # проверка на корректный url адрес
        assert "basket" in self.browser.current_url, "Basket url is not presented"
	
		#Ожидаем, что в корзине нет товаров
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.ITEMS_IN_BASKET), "Product is presented, but should not be"
	
		#Ожидаем, что в корзине нет надписи "Items to buy"
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.PRODUCT_IN_CART), "Message (Items to buy) is presented, but should not be"
		
		#Ожидаем, что есть текст о том что корзина пуста 
    def should_not_be_product_in_cart_message(self):
        assert self.is_element_present(*BasePageLocators.CART_IS_EMPTY_TEXT), "Message is not presented, but should not be"
		
		#ожидаем, что локатор совпадает с заголовком (корзина пуста)
    def should_not_be_product_in_cart_selector(self):
        basket_is_empty="Your basket is empty. Continue shopping"
        result = self.browser.find_element(*BasePageLocators.CART_IS_EMPTY_TEXT).text
        assert basket_is_empty == result, f"The locator '{result}' with the title indicating that there is no product '{basket_is_empty}' does not match"
		
