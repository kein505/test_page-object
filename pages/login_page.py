from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators
from .locators import BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "login" in self.browser.current_url, "Login url is not presented"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present (*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
		
    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present (*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"
		
    def register_new_user(self, email, password):
        mail = self.browser.find_element(*BasePageLocators.EMAIL_LINK)
        mail.send_keys(email)
        password1 = self.browser.find_element(*BasePageLocators.PASSWORD_LINK)
        password1.send_keys(password)
        password2 = self.browser.find_element(*BasePageLocators.CONFIRM_PASSWORD_LINK)
        password2.send_keys(password)
        regist_btn = self.browser.find_element(*BasePageLocators.REGISTRATION_BUTTON_LINK)
        regist_btn.click()
		
class AddPage(BasePage):
    def should_be_product_page(self):
	    #self.should_be_product_url()
	    self.should_be_add_product_to_cart_batton()
	    self.should_be_product_add_to_cart_message()
	    self.should_be_product_name_is_name_in_message()
	    self.should_be_cost_cart_message()
	    self.should_be_cost_cart_coincides_price_product()

    def should_be_product_url(self):
        # проверка на корректный url адрес
        assert "?promo=newYear" in self.browser.current_url, "parameter ?promo=newYear in url is not presented"

    def should_be_add_product_to_cart_batton(self):
        # проверка, что есть кнопка доавбления в корзину
        assert self.is_element_present (*ProductPageLocators.ADD_BUTTON), "Batton is not presented"

    def should_be_product_add_to_cart_message(self):
        # проверка, что есть сообщение, что товар добавлен в корзину.
        assert self.is_element_present (*ProductPageLocators.ADD_PRODUCT_MESSAGE), "Message is not presented"
		
    def should_be_product_name_is_name_in_message(self):
        # проверка, что название товара в сообщении совпадает с тем товаром, который вы действительно добавили.
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        message_add_product= self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_MESSAGE).text
        assert name_product == message_add_product, f"Название товара '{name_product}' в сообщении '{message_add_product}' не совпадает"
		
    def should_be_cost_cart_message(self):
        # проверка, что есть сообщение со стоимостью корзины
        assert self.is_element_present (*ProductPageLocators.COST_CART_MESSAGE), "The cost of the basket does not match the price of the goods"
		
    def should_be_cost_cart_coincides_price_product(self):
        # проверка, что стоимость корзины совпадает с ценой товара.
        cost_cart = self.browser.find_element(*ProductPageLocators.COST_CART).text
        price_product= self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert price_product == cost_cart, f"Стоимость корзины '{cost_cart}' с ценой товара '{price_product}' не совпадает"
		
		#is_not_element_present: упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый. 
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

		#is_disappeared будет ждать до тех пор, пока элемент не исчезнет
    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"