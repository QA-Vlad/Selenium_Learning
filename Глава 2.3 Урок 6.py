from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pyperclip


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME, "trollface").click()
    browser.switch_to.window(browser.window_handles[1])
    x = calc(int(browser.find_element(By.ID, "input_value").text))
    browser.find_element(By.ID, "answer").send_keys(x)
    browser.find_element(By.CLASS_NAME, "btn-primary").click()

    alert_text = browser.switch_to.alert.text
    alert_text = alert_text.split(': ')[-1]
    pyperclip.copy(alert_text)
    print(alert_text)

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()
