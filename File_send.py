from selenium import webdriver
import time
import os 

current_dir = os.path.abspath(os.path.dirname(__file__)) 
file_path = os.path.join(current_dir, 'file.txt')        

link="http://suninjuly.github.io/file_input.html"
browser=webdriver.Chrome()
browser.get(link)
browser.find_element_by_name("firstname").send_keys("alena")
browser.find_element_by_name("lastname").send_keys("kostina")
browser.find_element_by_name("email").send_keys("al@mail.ru")
browser.find_element_by_id("file").send_keys(file_path)
browser.find_element_by_css_selector("button.btn").click()
