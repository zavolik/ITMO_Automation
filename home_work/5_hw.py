#1 Создайте функцию которая переходит на страницу https://www.saucedemo.com/
# находит элементы: текстовое поле username, текстовое поле password, кнопку submit
# Создайте условие, если элементы найдены - вывести в консоль текст “Элементы найдены”

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
def open_site():
    driver.get("https://www.saucedemo.com/")
    try:
        driver.find_element(By.CSS_SELECTOR, '#user-name')
        driver.find_element(By.CSS_SELECTOR, '#password')
        driver.find_element(By.CSS_SELECTOR, '#login-button')
        print("Элементы найдены")
    except NoSuchElementException:
        print("Элементы не найдены")
open_site()
#все 3 элемента найдены