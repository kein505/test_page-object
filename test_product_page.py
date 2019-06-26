'''
1. Открываем страницу товара (http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear). Обратите внимание, что в ссылке есть параметр "?promo=newYear". Не теряйте его в авто-тесте, чтобы получить проверочный код.

2. Нажимаем на кнопку "Добавить в корзину".

3. *Посчитать результат математического выражения и ввести ответ. Используйте для этого метод solve_quiz_and_get_code(), который приведен ниже. Например, можете добавить его в класс BasePage, чтобы использовать его на любой странице. Этот метод нужен только для проверки того, что вы написали тест на Selenium. После этого вы получите код, который нужно ввести в качестве ответа на данное задание. Код будет выведен в консоли интерпретатора, в котором вы запускаете тест. Не забудьте в конце теста добавить проверки на ожидаемый результат.
'''
from .pages.product_page import ProductPage
import pytest
import time
#link1="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link2="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_can_add_product_to_cart(browser, link):
	page = ProductPage(browser, link)   # инициализируем Page Object, передаем конструктор экземпляр драйвера и url адрес 
	time.sleep(5)
	page.open()                      # открываем страницу
	time.sleep(5)	
	login_page = page.add_product_to_cart()          # выполняем метод страницы - Нажимаем на кнопку "Добавить в корзину"
	time.sleep(5)
	print("\nTyt login page:")
	login_page.should_be_product_page()
	time.sleep(5)
	print("\nstop Login Page..")