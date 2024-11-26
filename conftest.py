import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser(request):
    print("start browser")

    # Считываем значение параметра --language
    user_language = request.config.getoption("language")
    print(f"Выбранный язык: {user_language}")

    # Настройка языка для Chrome
    options = Options()
    #options.add_experimental_option('detach', True)
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)

    yield browser

    print("quit browser")
    browser.quit()

def pytest_addoption(parser):
    # Регистрация параметра --language
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose browser language"
    )