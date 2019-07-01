from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math

class BasePage(object):
	#инициализация страницы
    def __init__(self, browser, url, timeout=10):
	    self.browser = browser
	    self.url = url
	    self.browser.implicitly_wait(timeout)

	#метод открытия страницы
    def open(self): 
        self.browser.get(self.url)
	
	#метод перехода в корзину
    def go_to_cart_page(self):
        link = self.browser.find_element(*BasePageLocators.CART_LINK_BUTTON)
        link.click()#заходим в корзину

	#метод перехода на форму авторизации/регистрации	
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
		
	#is_disappeared будет ждать до тех пор, пока элемент не исчезнет			
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
            until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
	#метод проверки на присутствие элемента
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

	#is_not_element_present: тест упадет, как только увидит искомый элемент.
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
		
	#метод проверки, что пользователь авторизован			
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented,\n probably unauthorised user"
	
	#метод проверки, что поле логина присутствует на странице
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
	
	#метод в тесте для получения проверочного кода
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")