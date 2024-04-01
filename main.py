from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://googlechromelabs.github.io/chrome-for-testing/#stable")

input_element = driver.find_element(By.CLASS_NAME, "table-wrapper")
print(input_element.find_elements(By.TAG_NAME, "td"))
# input_element = driver.find_element(By.NAME, "q")

# input_element.send_keys("Hello World!" + Keys.ENTER)
# print(input_element.find_elements(By.TAG_NAME, "td"))
# print(dir(input_element))
print(input_element.size)

# time.sleep(5)

driver.quit()