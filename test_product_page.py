'''
1. Открываем страницу товара (http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear). Обратите внимание, что в ссылке есть параметр "?promo=newYear". Не теряйте его в авто-тесте, чтобы получить проверочный код.

2. Нажимаем на кнопку "Добавить в корзину".

3. *Посчитать результат математического выражения и ввести ответ. Используйте для этого метод solve_quiz_and_get_code(), который приведен ниже. Например, можете добавить его в класс BasePage, чтобы использовать его на любой странице. Этот метод нужен только для проверки того, что вы написали тест на Selenium. После этого вы получите код, который нужно ввести в качестве ответа на данное задание. Код будет выведен в консоли интерпретатора, в котором вы запускаете тест. Не забудьте в конце теста добавить проверки на ожидаемый результат.
'''
from .pages.product_page import ProductPage
from .pages.login_page import AddPage
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
	
'''
test_guest_cant_see_success_message: 
Открываем страницу товара 
Проверяем, что нет сообщения об успехе с помощью is_not_element_present
'''
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_cant_see_success_message(browser, link):
	page = ProductPage(browser, link)   # инициализируем Page Object, передаем конструктор экземпляр драйвера и url адрес 
	page.open()                      # открываем страницу	
	#see_success_page = page.add_product_to_cart()          # выполняем метод страницы - Нажимаем на кнопку "Добавить в корзину"
	print("\nTyt see_success_page:")
	AddPage(browser, link).should_not_be_success_message() #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
	print("\nstop see_success_page..")	
	
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