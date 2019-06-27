from .pages.product_page import ProductPage
import pytest
import time
#link1="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link2="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"#,
 #                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
  #                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
   #                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    #                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
     #                             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
      #                            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
       #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        #                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
         #                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
		 ])
def test_guest_can_add_product_to_cart(browser, link):
	page = ProductPage(browser, link)   # инициализируем Page Object, передаем конструктор экземпляр драйвера и url адрес 
	page.open()                      	# открываем страницу	
	login_page = page.add_product_to_cart()          # выполняем метод страницы - Нажимаем на кнопку "Добавить в корзину"
	login_page.should_be_product_page()
	
	#page.add_product_to_cart()
	#login_page = AddPage(browser, browser.current_url)
	#login_page.should_be_product_page()
	
'''
test_guest_cant_see_success_message: 
Открываем страницу товара 
Проверяем, что нет сообщения об успехе с помощью is_not_element_present
'''
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_cant_see_success_message(browser, link):
	page = ProductPage(browser, link)   # инициализируем Page Object, передаем конструктор экземпляр драйвера и url адрес 
	page.open()                      # открываем страницу	
	page.should_not_be_success() #Проверяем, что нет сообщения об успехе с помощью is_not_element_present

	
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

'''
1.Гость открывает главную страницу +
2.Переходит в корзину по кнопке в шапке сайта +
3.Ожидаем, что в корзине нет товаров
4.Ожидаем, что есть текст о том что корзина пуста 
'''	
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    page.should_not_be_product_in_cart()
    #cart_page = page.add_product_to_cart()          # выполняем метод страницы - Нажимаем на кнопку "Добавить в корзину"
    #cart_page.should_not_be_product_in_cart()