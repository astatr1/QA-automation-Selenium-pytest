import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: '--language=en' or '--language=ru'")


@pytest.fixture(scope="function")
def browser(request):
    set_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs',
                                    {'intl.accept_languages': set_language})
    options_firefox = webdriver.FirefoxOptions()
    options_firefox.add_argument("--language")
    browser_name = request.config.getoption('browser_name')

    if browser_name == 'chrome':
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome of firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
