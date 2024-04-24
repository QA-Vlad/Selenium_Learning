import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
#Что-бы работало быстрее, но кушало оперативу заменить, закомментировать строку выше и раскомментировать ниже
# @pytest.fixture(scope="class")
def browser():
    print("\nТест кейс начался")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nТест кейс окончился")
    browser.quit()
