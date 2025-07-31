import os
import sys
import pytest


from selenium import webdriver

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.allure_report_dir = "allure-results"

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                    help="Choose language for browser")
                    

@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    driver = None
    if browser_name == "chrome":
        print("\nstart browser Chrome for test..")
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.page_load_strategy = 'eager'
        #options.add_argument(f"--proxy-server={PROXY}")
        #options.add_argument('--no-sandbox')
        #options.add_argument('--start-maximized')
        options.add_argument('--headless')
        #options.add_argument('--disable-infobars')
        #options.add_argument('--disable-extensions')
        options.add_argument('--disable-gpu')
        #options.add_argument('--disable-dev-shm-usage')
        #options.add_argument('--incognito')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--window-size=1280,720')
        options.add_argument('--disable-cache')
        options.add_argument("--disable-blink-features=AutomationControlled")
        #options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
        preferences = {
            "download.default_directory" : os.path.join(os.getcwd(), "Google", "downloads") # Универсальный путь для всех систем
        #   "download.default_directory" : f"{os.getcwd()}\Google\downloads"
        }
        options.add_experimental_option("prefs", preferences)
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        from webdriver_manager.firefox import GeckoDriverManager
        from selenium.webdriver.firefox.service import Service
        from selenium.webdriver.firefox.options import Options
        options = Options()
        options.set_preference("intl.accept_languages", user_language)
        service = Service(GeckoDriverManager(version='v0.34.0').install())
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit browser..")
    driver.quit()

    