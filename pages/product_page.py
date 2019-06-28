from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import LoginPageLocators
from .login_page import LoginPage
from .login_page import AddPage
from .cart_page import CartPage
from selenium.webdriver.common.by import By


class ProductPage(BasePage): 
    def add_product_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        link.click()
        self.solve_quiz_and_get_code()
        return AddPage(browser=self.browser, url=self.browser.current_url)
		
    def should_not_be_success(self):
        AddPage(browser=self.browser, url=self.browser.current_url).should_not_be_success_message() #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
		
    def should_not_be_product_in_cart(self):
        CartPage(browser=self.browser, url=self.browser.current_url).should_be_cart_page() #Проверяем, что в корзине нет товара