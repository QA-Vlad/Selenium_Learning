from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "https://www.demo.guru99.com/V4/index.php"
login = "mngr567536"
password = "adUquvu"

try:
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    browser.get(link)

    browser.find_element(By.NAME, "uid").send_keys(login)
    browser.find_element(By.NAME, "password").send_keys(password)
    browser.find_element(By.NAME, "btnLogin").click()
finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()
