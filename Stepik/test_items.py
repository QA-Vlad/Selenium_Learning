from selenium.webdriver.common.by import By
import time

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_buy_button(browser):
    browser.get(link)
    buy_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert buy_button.is_displayed()
    time.sleep(30)
