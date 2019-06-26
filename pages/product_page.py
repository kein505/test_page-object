from .base_page import BasePage
from .locators import AddToCartLocators
from .login_page import AddPage
from selenium.webdriver.common.by import By


class ProductPage(BasePage): 
    def add_product_to_cart(self):
        link = self.browser.find_element(*AddToCartLocators.ADD_BUTTON)
        link.click()
        self.solve_quiz_and_get_code()
        return AddPage(browser=self.browser, url=self.browser.current_url)