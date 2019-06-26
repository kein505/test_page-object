from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators


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
        name_product = self.give_element_present(*ProductPageLocators.NAME_PRODUCT).text
        print("\nproduct_name\n", name_product)
        message_add_product= self.give_element_present(*ProductPageLocators.ADD_PRODUCT_MESSAGE).text
        print("\nmessage_add_product\n", message_add_product)
        assert name_product in message_add_product, f"Название товара '{name_product}' в сообщении '{message_add_product}' не совпадает"
		
    def should_be_cost_cart_message(self):
        # проверка, что есть сообщение со стоимостью корзины
        assert self.is_element_present (*ProductPageLocators.COST_CART_MESSAGE), "The cost of the basket does not match the price of the goods"
		
    def should_be_cost_cart_coincides_price_product(self):
        # проверка, что стоимость корзины совпадает с ценой товара.
        cost_cart = self.give_element_present(*ProductPageLocators.COST_CART).text #[38:43]
        print("\ncost_cart", cost_cart)
        price_product= self.give_element_present(*ProductPageLocators.PRICE_PRODUCT).text #[0:5]
        print("\nprice_product", price_product)
        assert price_product in cost_cart, f"Стоимость корзины '{cost_cart}' с ценой товара '{price_product}' не совпадает"