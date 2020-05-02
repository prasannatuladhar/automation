# reference:https://selenium-python.readthedocs.io/waits.html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.letzcricket.com/")
print(driver.title)
link = driver.find_element_by_link_text("Predictions, Probable XI - New Zealand vs India 2nd T20")
link.click()
print(driver.title)
all_data = driver.find_elements_by_tag_name("p")
for data in all_data:
    print(data.text)
    print("************")

driver.close()