from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")				#локатор логина
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid") #локатор неверного логина
	
class LoginPageLocators(object):
	LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link") #локатор логина
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") 		#локатор неверного логина
	REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form") #локатор формы регистрации
	
class ProductPageLocators(object):
	ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")#локатор кнопки добавления в карзину
	ADD_PRODUCT_MESSAGE = (By.CSS_SELECTOR, ".alert-success.fade.in:nth-child(1)>div.alertinner>strong")#локатор сообщения о добовлении продукта в карзину
	NAME_PRODUCT = (By.TAG_NAME, "h1")	#локатор названия продукта
	COST_CART_MESSAGE = (By.CSS_SELECTOR, ".alert-info.fade.in")#локатор сообщения со стоимостью корзины
	COST_CART = (By.CSS_SELECTOR, ".alert-info.fade.in>div.alertinner>p>strong")#локатор сообщение стоимости корзины
	PRICE_PRODUCT = (By.CSS_SELECTOR, '[class="price_color"]')#локатор стоимости продукта
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-success.fade.in')#локатор сообщение успешном добоалвении продукта в корзину
	
class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")#локатор логина
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")#локатор неверного логина
    CART_LINK_BUTTON = (By.CSS_SELECTOR, ".btn-group>a.btn.btn-default")#локатор кнопки входа в корзину
    CART_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "div#content_inner>p")#сообщение -корзина пуста ("Your basket is empty. Continue shopping")
    PRODUCT_IN_CART = (By.CSS_SELECTOR, "h2.col-sm-6.h3") #сообщение- "Items to buy" 
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items") # локатор присутствия продуктво в корзине
    EMAIL_LINK = (By.CSS_SELECTOR, "[id='id_registration-email']")#локатор поля ввода email
    PASSWORD_LINK = (By.CSS_SELECTOR, "[id='id_registration-password1']")#локатор поля ввода пароля
    CONFIRM_PASSWORD_LINK = (By.CSS_SELECTOR, "[id='id_registration-password2']")#локатор поля ввода подвтерждения пароля
    REGISTRATION_BUTTON_LINK = (By.CSS_SELECTOR, '[name="registration_submit"]')#локатор кнопки регистрации
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")#локатор пользователь залогинен