from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
import time
import math
import unittest
from selenium.webdriver.common.by import By

link0="http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
link1="http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer1"
link2="http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer2"
link3="http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer3"
link4="http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer4"
link5="http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer5"
link6="http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer6"
link7="http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer7"
link8="http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer8"
link9="http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer9"




print("\nstart browser for test..")
browser = webdriver.Chrome()
browser.get(link0)

browser.find_element_by_css_selector('#add_to_basket_form').click()
time.sleep(1)


print("\nstart SCHITOVOD..")

alert = browser.switch_to.alert
x = alert.text.split(" ")[2]
answer = str(math.log(abs((12 * math.sin(float(x))))))
alert.send_keys(answer)
alert.accept()
try:
    alert = browser.switch_to.alert
    print("Your code: {}".format(alert.text))
    alert.accept()
except NoAlertPresentException:
    print("No second alert presented")

print("\nstOP SCHITOVOD..")

'''
Ожидаемый результат: 

1. Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
2. Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
'''
#assert "?promo=newYear" in browser.current_url, "parameter ?promo=newYear in url is not presented"
#NAME_PRODUCT = (By.TAG_NAME, "h1")
product_name = browser.find_element(By.TAG_NAME, "h1").text
print("\nproduct_name\n", product_name)
#"The shellcoder's handbook был добавлен в вашу корзину."
message_add_product= browser.find_element_by_css_selector('.alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1)').text #[1:16]
print("\nmessage_add_product\n", message_add_product)
assert product_name in message_add_product, f"Название товара '{product_name}' в сообщении '{message_add_product}' не совпадает"
print("\n--------------------------------------------")
cost_cart = browser.find_element_by_css_selector('.alert.alert-safe.alert-noicon.alert-info.fade.in').text[38:43]
print("\ncost_cart", cost_cart)
price_product= browser.find_element_by_css_selector('[class="price_color"]').text[0:5]
print("\nprice_product", price_product)
assert price_product == cost_cart, f"Стоимость корзины '{cost_cart}' с ценой товара '{price_product}' не совпадает"
#result=

#expect_result=
#substring="The shellcoder's handbook был добавлен в вашу корзину."

#assert result == product_name, f"expected '{substring}' to be substring of '{full_string}'"