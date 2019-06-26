from .base_page import BasePage
from .locators import LoginPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By

class MainPage(BasePage): 
    def go_to_login_page(self):
        link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        link.click()
        #alert = self.browser.switch_to.alert
        #alert.accept()
        return LoginPage(browser=self.browser, url=self.browser.current_url) 
    	
    #def should_be_login_link(self):
     #   assert self.is_element_present (*LoginPageLocators.LOGIN_LINK), "Login link is not presented"