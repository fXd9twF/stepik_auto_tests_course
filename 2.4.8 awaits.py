import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    print(1)
    submit = browser.find_element(By.ID, 'book')
    submit.click()
    print(2)
    x = browser.find_element(By.ID, 'input_value')
    x = x.text
    print(x)
    y = str(math.log(abs(12*math.sin(int(x)))))
    print(4)
    text_box = browser.find_element(By.CSS_SELECTOR, 'input[required]')
    text_box.send_keys(y)
    print(5)
    button = browser.find_element(By.ID, 'solve')
    button.click()
    print(6)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(22)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла