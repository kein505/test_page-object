from .pages.main_page import MainPage
from .pages.cart_page import CartPage
import pytest
	
'''
1.Гость открывает главную страницу 
2.Переходит в корзину по кнопке в шапке сайта 
3.Ожидаем, что в корзине нет товаров
4.Ожидаем, что есть текст о том что корзина пуста 
'''
def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_cart_page()
    product = CartPage(browser, browser.current_url)
    product.should_not_be_product_in_cart() #Проверяем, что в корзине нет товара
	
@pytest.mark.login_guest
class TestLoginFromMainPage(object):                      
    def test_guest_can_go_to_login_link(self, browser):     
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
        page.should_be_login_link() 	#проверяем, что поле логина присутствует на странице

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


