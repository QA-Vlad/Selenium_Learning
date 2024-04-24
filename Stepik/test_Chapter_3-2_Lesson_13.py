from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAbc(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(10)
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        # На самом деле мой код падает уже на строке выше, ибо "разработчики" поменяли имя placeholder
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        input3.send_keys("petrov@gmail.com")
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы

        # находим элемент, содержащий текст и записываем в переменную welcome_text
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 'Welcome text not found')
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        # На самом деле мой код падает уже на строке выше, ибо "разработчики" поменяли имя placeholder
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        input3.send_keys("petrov@gmail.com")
        time.sleep(1)
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст и записываем в переменную welcome_text
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 'Welcome text not found')
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()
