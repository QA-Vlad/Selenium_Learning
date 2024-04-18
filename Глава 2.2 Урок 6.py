from selenium import webdriver
from selenium.webdriver.common.by import By
# import time
import math
import pyperclip

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/execute_script.html")
    x = calc(int(browser.find_element(By.ID, "input_value").text))
    browser.find_element(By.ID, "answer").send_keys(x)
    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    browser.find_element(By.CLASS_NAME, "btn-primary").location_once_scrolled_into_view
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    browser.find_element(By.CLASS_NAME, "btn-primary").click()

    alert_text = browser.switch_to.alert.text
    alert_text = alert_text.split(': ')[-1]
    pyperclip.copy(alert_text)
    print(alert_text)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()