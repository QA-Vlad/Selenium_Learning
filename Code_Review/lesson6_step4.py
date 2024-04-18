from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/registration2.html")
    elements = browser.find_elements(By.CSS_SELECTOR, 'input[type = "text"]')
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.XPATH, '//button[text() = "Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
