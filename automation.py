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
search = driver.find_element_by_name("q")
search.send_keys("nepal")
search.send_keys(Keys.RETURN)
try:
    news = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "news"))
    )
    articles = news.find_elements_by_class_name("media-body")
    for article in articles:
        header = article.find_elements_by_class_name("media-heading")
        print(header[0].text)
finally:
    driver.quit()



driver.close()