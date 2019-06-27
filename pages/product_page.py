from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import LoginPageLocators
from .login_page import AddPage
from selenium.webdriver.common.by import By


class ProductPage(BasePage): 
    def add_product_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        link.click()
        self.solve_quiz_and_get_code()
        return AddPage(browser=self.browser, url=self.browser.current_url)
		
    #def should_be_login_link(self):
     #   assert self.is_element_present (*LoginPageLocators.LOGIN_LINK), "Login link is not presented"