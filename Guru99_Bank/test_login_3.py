from selenium.webdriver.common.by import By
import pytest

link = "https://www.demo.guru99.com/V4/index.php"

valid_login = "mngr567536"
valid_password = "adUquvu"

invalid_login = "mngr567532"
invalid_password = "adUquvu1"


class Test_logins():
    @pytest.mark.logins
    def test_valid_login_and_password(self, browser):
        browser.get(link)

        browser.find_element(By.NAME, "uid").send_keys(valid_login)
        browser.find_element(By.NAME, "password").send_keys(valid_password)
        browser.find_element(By.NAME, "btnLogin").click()

        welcome_text = browser.find_element(By.CSS_SELECTOR, "[behavior='alternate']").text
        expected_text = "Welcome To Manager's Page of Guru99 Bank"
        assert welcome_text == expected_text, f"Expected text was '{expected_text}', but got '{welcome_text}'"

    @pytest.mark.logins
    def test_invalid_login_and_valid_password(self, browser):
        browser.get(link)

        browser.find_element(By.NAME, "uid").send_keys(invalid_login)
        browser.find_element(By.NAME, "password").send_keys(valid_password)
        browser.find_element(By.NAME, "btnLogin").click()

        alert = browser.switch_to.alert
        alert_text = alert.text
        assert alert_text == "User or Password is not valid", "No expected error about invalid login or password"
        alert.accept()

    @pytest.mark.logins
    def test_valid_login_and_invalid_password(self, browser):
        browser.get(link)

        browser.find_element(By.NAME, "uid").send_keys(valid_login)
        browser.find_element(By.NAME, "password").send_keys(invalid_password)
        browser.find_element(By.NAME, "btnLogin").click()

        alert = browser.switch_to.alert
        alert_text = alert.text
        assert alert_text == "User or Password is not valid", "No expected error about invalid login or password"
        alert.accept()

    @pytest.mark.logins
    def test_invalid_login_and_invalid_password(self, browser):
        browser.get(link)

        browser.find_element(By.NAME, "uid").send_keys(invalid_login)
        browser.find_element(By.NAME, "password").send_keys(invalid_password)
        browser.find_element(By.NAME, "btnLogin").click()

        alert = browser.switch_to.alert
        alert_text = alert.text
        assert alert_text == "User or Password is not valid", "No expected error about invalid login or password"
        alert.accept()
