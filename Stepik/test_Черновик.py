import pytest


languages = [
    ("ru", "русский"),
    ("de" "немецкий"),
    ("ua", "украинский"),
    ("en-gb", "английский")
]


@pytest.mark.parametrize("code, lang", languages)
def test_guest_should_see_login_link(browser, code, lang):
    link = "http://selenium1py.pythonanywhere.com/{}/".format(code)
    print("Проверяемый язык %s" % lang)