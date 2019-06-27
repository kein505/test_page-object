from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")
	
class LoginPageLocators(object):
	LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
	
class ProductPageLocators(object):
	ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
	ADD_PRODUCT_MESSAGE = (By.CSS_SELECTOR, ".alert-success.fade.in:nth-child(1)>div.alertinner>strong")
	NAME_PRODUCT = (By.TAG_NAME, "h1")
	COST_CART_MESSAGE = (By.CSS_SELECTOR, ".alert-info.fade.in")
	COST_CART = (By.CSS_SELECTOR, ".alert-info.fade.in>div.alertinner>p>strong")
	PRICE_PRODUCT = (By.CSS_SELECTOR, '[class="price_color"]')
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
	
class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")