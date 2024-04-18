from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/registration2.html')

try:
    first = browser.find_element(By.CLASS_NAME, 'first_block').find_element(By.CLASS_NAME, 'first')
    first.send_keys('Ivan')
    last = browser.find_element(By.CLASS_NAME, 'first_block').find_element(By.CLASS_NAME, 'second')
    last.send_keys('Petrov')
    mail = browser.find_element(By.CLASS_NAME, 'first_block').find_element(By.CLASS_NAME, 'third')
    mail.send_keys('dlkl@mail.com')
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(30)
    browser.quit()