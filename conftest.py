import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en-us, fr or ru")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--lang={}".format(user_language))
    browser = webdriver.Chrome(options=chrome_options)

    yield browser

    print("\nquit browser..")
    browser.quit()
