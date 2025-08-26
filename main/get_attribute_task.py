from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Открыть страницу
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти элемент-картинку, который является изображением сундука с сокровищами
    treasure = browser.find_element(By.ID, "treasure")
    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи
    x = treasure.get_attribute("valuex")
    # Посчитать математическую функцию от x
    y = calc(x)

    # Ввести ответ в текстовое поле
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    # Отметить checkbox "I'm the robot"
    option_checkbox = browser.find_element(By.ID, "robotCheckbox")
    option_checkbox.click()

    # Выбрать radiobutton "Robots rule!"
    option_radio = browser.find_element(By.ID, "robotsRule")
    option_radio.click()

    # Нажать на кнопку "Submit"
    button_submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()