import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/math.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    text_box = browser.find_element(By.CSS_SELECTOR, 'input[required]')
    text_box.send_keys(y)
    time.sleep(0.5)
    check_box = browser.find_element(By.ID, 'robotCheckbox')
    check_box.click()
    time.sleep(0.5)
    rob_rule = browser.find_element(By.ID,'robotsRule')
    rob_rule.click()
    time.sleep(0.5)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(22)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла