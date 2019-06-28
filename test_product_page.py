from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest
import time
#link1="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link2="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
'''
link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

@pytest.mark.login
class TestLoginFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.product = ProductFactory(title = "Best book created by robot")
        # создаем по апи
        self.link = self.product.link
        yield
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали 
        self.product.delete()
        

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        print("\n test_guest_should_see_login_link")
        page.should_be_login_link()
'''





#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"#,
 #                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
  #                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
   #                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    #                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
     #                             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
      #                            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
       #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        #                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
         #                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
#		 ])	
	
'''
Добавьте в класс фикстуру setup. В этой функции нужно:
1.открыть страницу регистрации
2.зарегистрировать нового пользователя
3.проверить, что пользователь залогинен
'''

class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        self.page = ProductPage(browser, link)   # инициализируем Page Object, передаем конструктор экземпляр драйвера и url адрес 
        self.page.open()                      # открываем страницу        
        self.page.go_to_login_page()		#открыть страницу регистраци
        email = str(time.time()) + "@fakemail.org" #создание адреса почты
        print("email: ", email)
        password="Pas5word9"				#пароль
        reg_user = LoginPage(browser, browser.current_url)
        reg_user.register_new_user1(email, password) #регистрируем пользователя
        self.page.should_be_authorized_user() #проверка, что пользователь залогинен

		
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser,  link)   # инициализируем Page Object, передаем конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу	
        page.should_not_be_success() #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
		
    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser,  link)   # инициализируем Page Object, передаем конструктор экземпляр драйвера и url адрес 
        page.open()                      	# открываем страницу	
        login_page = page.add_product_to_cart()          # выполняем метод страницы - Нажимаем на кнопку "Добавить в корзину"
        login_page.should_be_product_page()

#гость может добавить продкут в корзину, проверка , что продукт в корзине
@pytest.mark.need_review		
def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser,  link)   # инициализируем Page Object, передаем конструктор экземпляр драйвера и url адрес 
    page.open()                      	# открываем страницу	
    login_page = page.add_product_to_cart()   # выполняем метод страницы - Нажимаем на кнопку "Добавить в корзину"
    login_page.should_be_product_page()  #проверка  

'''
1.Гость открывает главную страницу 
2.Переходит в корзину по кнопке в шапке сайта 
3.Ожидаем, что в корзине нет товаров
4.Ожидаем, что есть текст о том что корзина пуста 
'''	
@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    page.should_not_be_product_in_cart()#Проверяем, что в корзине нет товара

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

	
'''


---------
test_guest_cant_see_success_message: 
Открываем страницу товара 
Проверяем, что нет сообщения об успехе с помощью is_not_element_present
'''

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_cant_see_success_message(browser, link):
	page = ProductPage(browser, link)   # инициализируем Page Object, передаем конструктор экземпляр драйвера и url адрес 
	page.open()                      # открываем страницу	
	page.should_not_be_success() #Проверяем, что нет сообщения об успехе с помощью is_not_element_present

'''
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


'''
	
