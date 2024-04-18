from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pyperclip
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, "book").click()
    x = calc(int(browser.find_element(By.ID, "input_value").text))
    browser.find_element(By.ID, "answer")
    browser.find_element(By.ID, "solve").click()
    alert_text = browser.switch_to.alert.text
    alert_text = alert_text.split(': ')[-1]
    pyperclip.copy(alert_text)
    print(alert_text)

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()
