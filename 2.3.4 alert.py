import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    acc1 = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    acc1.click()
    print(1)
    confirm = browser.switch_to.alert
    confirm.accept()
    print(2)
    x = browser.find_element(By.ID, 'input_value')
    x = x.text
    print(3)
    y = str(math.log(abs(12*math.sin(int(x)))))
    print(4)
    text_box = browser.find_element(By.CSS_SELECTOR, 'input[required]')
    text_box.send_keys(y)
    print(5)
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
    print(6)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(22)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла