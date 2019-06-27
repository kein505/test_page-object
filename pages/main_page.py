from .base_page import BasePage
from .locators import LoginPageLocators
from .login_page import LoginPage
from .cart_page import CartPage
from selenium.webdriver.common.by import By

class MainPage(BasePage): 
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
		
    def should_not_be_product_in_cart(self):
        CartPage(browser=self.browser, url=self.browser.current_url).should_be_cart_page() #Проверяем, что в корзине нет товара