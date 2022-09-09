from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time 



link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text
    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text
    z = str(int(x) + int(y))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(z)
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    browser.quit()
