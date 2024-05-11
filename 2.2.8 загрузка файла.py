import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt') # добавляем к этому пути имя файла


try:
    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element(By.NAME, 'firstname')
    first.send_keys('Ivan')
    time.sleep(0.3)
    print(1)
    last = browser.find_element(By.NAME, 'lastname')
    last.send_keys('Drogo')
    time.sleep(0.3)
    print(2)
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('fuck you email')
    time.sleep(0.3)
    print(3)
    upload_button = browser.find_element(By.ID, 'file')
    upload_button.send_keys(file_path)
    time.sleep(0.3)
    print(4)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    print(5)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(22)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла