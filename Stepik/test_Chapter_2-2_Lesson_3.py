from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time



try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")
    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)
    operator = browser.find_element(By.CSS_SELECTOR, ".nowrap:nth-child(3)").text
    select = Select(browser.find_element(By.ID, "dropdown"))

    if operator in ["+", "и"]:
        result = num1 + num2
        result = str(result)
    elif operator == "-":
        result = num1 - num2
        result = str(result)
    elif operator == "/":
        result = num1 / num2
        result = str(result)
    elif operator == "*":
        result = num1 * num2
        result = str(result)
    else:
        print('Не найден поддерживаемый оператор')

    select.select_by_value(result)
    browser.find_element(By.CSS_SELECTOR, '.btn-default').click()
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

