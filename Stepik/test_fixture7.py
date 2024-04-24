import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


languages = ["ru", "en-gb"]  # Можно добавить больше языков по желанию


@pytest.mark.parametrize("lang", languages)
def test_guest_should_see_login_link(browser, lang):
    link = f"https://selenium1py.pythonanywhere.com/{lang}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
