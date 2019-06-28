from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasePageLocators


class CartPage(BasePage):
    def should_be_cart_page(self):
        self.should_be_basket_url()
        self.should_not_be_product_in_cart()
        self.should_not_be_product_in_cart_message()
        self.should_not_be_product_in_cart_selector()

    def should_be_basket_url(self):
        # проверка на корректный url адрес
        assert "basket" in self.browser.current_url, "Basket url is not presented"
	
		#Ожидаем, что в корзине нет товаров
    def should_not_be_product_in_cart(self):
        assert self.is_not_element_present(*BasePageLocators.PRODUCT_IN_CART), "Product is presented, but should not be"
		
		#Ожидаем, что есть текст о том что корзина пуста 
    def should_not_be_product_in_cart_message(self):
        assert self.is_element_present(*BasePageLocators.CART_IS_EMPTY_TEXT), "Message is not presented, but should not be"
		
		#ожидаем, что селектор совпадает с заголовком (корзина пуста)
    def should_not_be_product_in_cart_selector(self):
        basket_is_empty="Your basket is empty. Continue shopping"
        result = self.give_element_present(*BasePageLocators.CART_IS_EMPTY_TEXT).text
        assert basket_is_empty == result, f"Селектор '{result}'с заголовком о том что товара нет '{basket_is_empty}' совпадает"

 #   def should_be_product_in_cart(self):
  #      assert self.is_element_present(*BasePageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
		
   # def should_be_product_in_cart_message(self):
    #    assert self.is_element_present(*BasePageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"