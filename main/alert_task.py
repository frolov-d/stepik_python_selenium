import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyperclip as pc

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    time.sleep(1)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    button_submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_submit.click()

    # сохранить в буфер
    pc.copy(browser.switch_to.alert.text.split(': ')[-1])

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
