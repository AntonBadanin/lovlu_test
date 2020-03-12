import pytest
from pytest import fixture
from selenium import webdriver
import allure
import logging
import os

PHONE_LIST = {"iphone10": "iPhone X", "samsung": "Galaxy S5", "iphone678": "iPhone 6/7/8 Plus", "ipad": "iPad"}


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


def pytest_addoption(parser):
    parser.addoption('--mobile', action='store', default=None,
                     help="Choose language: iPhone or Samsung")


# Основная функция с настройками тестов
@pytest.fixture(scope="function")
def browser(request):
    chrome_options = webdriver.ChromeOptions()
    mobile_emulation = request.config.getoption("mobile")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    print("\nstart browser..")
    if mobile_emulation in PHONE_LIST.keys():
        chrome_options.add_experimental_option("mobileEmulation", {"deviceName": PHONE_LIST[mobile_emulation]})
        print(f"Параметр запуска: телефон - {PHONE_LIST[mobile_emulation]}")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    if mobile_emulation == "desktop":
        driver.set_window_size(1920, 1080)
        print(f"Параметр запуска: десктоп 1920*1080")
    yield driver
    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            driver.execute_script("document.body.bgColor = 'white';")
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
        except:
            pass  # just ignore
    print("\nquit browser..")
    driver.quit()


@pytest.fixture(scope='session')
def baseurl(request):
    baseurl = os.environ.get('BASEURL')
    return baseurl


@pytest.fixture(scope='session')
def username(request):
    username = os.environ.get('USERNAME')
    return username


@pytest.fixture(scope='session')
def password(request):
    password = os.environ.get('PASSWORD')
    return password


@pytest.fixture(scope='session')
def token(request):
    token = os.environ.get('TOKEN')
    return token
