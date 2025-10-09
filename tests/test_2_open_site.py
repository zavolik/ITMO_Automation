from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome( )
driver.get("https:/demoqa.com/")

# поиск элемента
time.sleep(5)
icon = driver.find_element(By.CSS_SELECTOR, 'header > a > img')
if icon is None:
    print('Элемент не найден')
else:
    print ('Элемент найден')