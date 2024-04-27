from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import json
import time
import math

# Путь к вашему JSON-файлу
json_file = 'Stepik/logins.json'

# Открываем файл и загружаем данные в словарь
with open(json_file, 'r') as f:
    data = json.load(f)

# Теперь данные доступны в словаре data
login_stepik = data['login_stepik']
password_stepik = data['password_stepik']

#Ссылки
links = ("https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1")


@pytest.mark.parametrize("link", links)
def test_login_stepik(browser, link):
    wait_submission = WebDriverWait(browser, 90)
    wait_final_text = WebDriverWait(browser, 20)
    wait_again_btn = WebDriverWait(browser, 5)
    wait_send_btn = WebDriverWait(browser, 10)

    browser.get(link)
    # Ждём пока загрузится кнопка отправить или повторить. Она обычно самой последней подгружается
    wait_submission.until(EC.presence_of_element_located((By.CLASS_NAME, "submit-submission" or "again-btn")))

    # Логинимся
    browser.find_element(By.CLASS_NAME, 'navbar__auth_login').click()
    browser.find_element(By.NAME, 'login').send_keys(login_stepik)
    browser.find_element(By.NAME, 'password').send_keys(password_stepik)
    browser.find_element(By.CLASS_NAME, 'sign-form__btn').click()

    #Дожидаемся пока окно авторизации пропадёт
    wait_submission.until(EC.staleness_of(browser.find_element(By.CLASS_NAME, 'modal-button-close-icon')))

    # Проверяем, не был ли ранее отправлен ответ. Если был, то жмём кнопку повторить
    try:
        again_btn_present = wait_again_btn.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.again-btn")))
        # Если кнопка найдена, то кликаем
        again_btn_present.click()
        # Ну и проверяем нет ли окна "Вы уверены?"
        try:
            confirm_btn_present\
                = wait_again_btn.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".modal-popup__container  button:nth-child(1)")))
            confirm_btn_present.click()
        except TimeoutException:
            # Если кнопка отсутствует, просто продолжаем прогон.
            pass
    except TimeoutException:
        # Если кнопка отсутствует, просто продолжаем прогон.
        pass

    # Отправляем правильный ответ
    time.sleep(1)  # Без этой паузы у меня время от времени расходится время компа и сайта
    answer = math.log(int(time.time()))
    browser.find_element(By.CLASS_NAME, "ember-text-area").send_keys(answer)

    #Ждём появление кнопки отправки
    wait_send_btn.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".attempt__actions .submit-submission")))
    # Кликаем по ней
    time.sleep(1)
    browser.find_element(By.CLASS_NAME, "submit-submission").click()

    # Ждём пока появится финальный текст
    wait_final_text.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".lesson__hint > p")))

    # Проверяем, что текст внутри .lesson__hint > p текст   равен "Correct!"
    finish_text = browser.find_element(By.CSS_SELECTOR, '.lesson__hint > p').text
    assert finish_text == 'Correct!', f'Ожидали  "Correct!" а получили "{finish_text}"'

    time.sleep(3)
