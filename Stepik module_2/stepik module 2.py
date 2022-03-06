from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math
import os

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    #browser.implicitly_wait(15)
    browser.get(link)


    #price = browser.find_element("id", "price")
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element(("id", "price"), "100")
    )
    submit = file_upload = browser.find_element("class name", "btn").click()

    x_value = browser.find_element("id", "input_value")
    x = int(x_value.text)
    y = math.log(abs(12 * math.sin(x)))

    input_y = browser.find_element("id", "answer")
    input_y.send_keys(y)
    submit = browser.find_element("id", "solve").click()

    alert = browser.switch_to.alert
    print(alert.text)
    # first_name.send_keys("Alex")
    # last_name = browser.find_element("name", "lastname")
    # last_name.send_keys("Skudarnov")
    # email = browser.find_element("name", "email")
    # email.send_keys("Skudarnov@test.ru")
    # file_upload = browser.find_element("name", "file")
    # file_upload.send_keys(file_path)


    #browser.switch_to.window(first_window)
    #new_window = browser.window_handles[1]
    # first_window = browser.window_handles[0]

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
