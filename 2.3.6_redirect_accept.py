from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()
    browser.switch_to.window(browser.window_handles[1])
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    z = calc(int(x))
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(z)
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    browser.quit()
