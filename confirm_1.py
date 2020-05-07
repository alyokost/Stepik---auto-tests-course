from selenium import webdriver
import time
import os 
import math


link=" http://suninjuly.github.io/alert_accept.html"

try:
    browser=webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector("button.btn").click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element_by_id("input_value").text
    y = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element_by_tag_name("input").send_keys(y)
    browser.find_element_by_css_selector("button.btn").click()
finally:
    time.sleep(15)
    browser.quit()
