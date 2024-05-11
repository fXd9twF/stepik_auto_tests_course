import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    but1 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    but1.click()
    print(1)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, 'input_value')
    x = x.text
    print(2)
    y = str(math.log(abs(12*math.sin(int(x)))))
    print(3)
    text_box = browser.find_element(By.CSS_SELECTOR, 'input[required]')
    text_box.send_keys(y)
    print(4)
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
    print(5)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(22)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла