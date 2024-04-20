from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAbc(unittest.TestCase):
    def test_login(self):
        link = "https://www.demo.guru99.com/V4/index.php"
        login = "mngr567536"
        password = "adUquvu"

        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)

        browser.find_element(By.NAME, "uid").send_keys(login)
        browser.find_element(By.NAME, "password").send_keys(password)
        browser.find_element(By.NAME, "btnLogin").click()

        welcome_text = browser.find_element(By.CSS_SELECTOR, "[behavior='alternate']").text
        expected_text = "Welcome To Manager's Page of Guru99 Bank"
        self.assertEqual(expected_text, welcome_text, f"Expected text was '{expected_text}', but got '{welcome_text}'")
        # закрываем браузер после всех манипуляций
        time.sleep(4)
        browser.quit()
