from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "https://suninjuly.github.io/file_input.html"


current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("ivan.petrov@gmail.com")
    browser.find_element(By.ID, "file").send_keys(file_path)
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()


finally:
    time.sleep(10)
    browser.quit()

# не забываем оставить пустую строку в конце файла
