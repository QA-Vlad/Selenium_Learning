from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_buy_button(browser):
    browser.get(link)

    try:
        # Явное ожидание появления кнопки на странице
        buy_button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn-add-to-basket"))
        )
    except TimeoutException:
        # Если элемент не был найден за 10 секунд, выводим соответствующее сообщение
        print(f"Элемент с селектором {By.CLASS_NAME, 'btn-add-to-basket'} не был найден на странице {link}")
        raise
    else:
        # Проверка, что кнопка отображается
        assert buy_button.is_displayed(), "Кнопка 'Добавить в корзину' не отображается"

    time.sleep(30)  # Визуальная проверка языка сайта
