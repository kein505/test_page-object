from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")
	
class LoginPageLocators(object):
	#LOGIN_url = (By.CSS_SELECTOR, "login")
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
	
class AddToCartLocators(object):
	ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
	ADD_PRODUCT_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1)")
	NAME_PRODUCT = (By.TAG_NAME, "h1")
	COST_CART_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in")
	COST_CART = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in")
	PRICE_PRODUCT = (By.CSS_SELECTOR, '[class="price_color"]')