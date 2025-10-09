#1 Создайте функцию которая переходит на страницу https://www.saucedemo.com/
# находит элементы: текстовое поле username, текстовое поле password, кнопку submit
# Создайте условие, если элементы найдены - вывести в консоль текст “Элементы найдены”

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# поиск элемента
text_area_username = driver.find_element(By.CSS_SELECTOR, '#user-name')
text_area_password = driver.find_element(By.CSS_SELECTOR, '#password')
button_submit = driver.find_element(By.CSS_SELECTOR, '#login-button')
if (text_area_username is None) and (text_area_password is None) and (button_submit is None):
    print('Элементы не найдены')
else:
    print ('Элементы найдены')

#все 3 элемента найдены