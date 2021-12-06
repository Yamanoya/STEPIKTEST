from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")


dollars = WebDriverWait(browser,12).until(
        EC.text_to_be_present_in_element((By.XPATH,"//h5[@id='price']"),"$100"))
button = browser.find_element_by_xpath("//button[@id='book']")
button.click()

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
finally:
    number = browser.find_element_by_xpath("//span[@id='input_value']").text
    x = number
    y = calc(x)

    feild = browser.find_element_by_xpath("//input[@id='answer']")
    feild.click()
    feild.send_keys(y)


    but = browser.find_element_by_xpath("//button[@id='solve']")
    but.click()

    time.sleep(5)


