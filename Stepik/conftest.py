import pytest
from selenium import webdriver


print("conftest.py is loaded")


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")  # Выбор браузера в командной строке: pytest --browser_name=firefox
    parser.addoption('--language', action='store', default='fr',  #Выбор языка в командной строке --language=ru
                     help='Choose language: es or fr or en or ru')


@pytest.fixture(scope="function")
# #Что-бы работало быстрее, но кушало оперативу заменить, закомментировать строку выше и раскомментировать ниже
# @pytest.fixture(scope="class")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        print("\nТест кейс в Хроме начался...")
        options = webdriver.ChromeOptions()
        options.add_argument(f'--lang={user_language}')
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nТест кейс в Фаерфох начался...")
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=firefox_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nТест кейс окончился")
    browser.quit()
