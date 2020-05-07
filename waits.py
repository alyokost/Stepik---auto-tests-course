from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import os 
import math


link="http://suninjuly.github.io/explicit_wait2.html"

try:
    browser=webdriver.Chrome()
    browser.get(link)
    WebDriverWait(browser, 30).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_css_selector("button.btn").click()
    x = browser.find_element_by_id("input_value").text
    y = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element_by_tag_name("input").send_keys(y)
    browser.find_element_by_id("solve").click()
finally:
    time.sleep(15)
    browser.quit()
