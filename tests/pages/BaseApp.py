import allure
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.base_url = url

    # Открываем страницу
    def open(self):
        with allure.step(f'Переходим на страницу {self.base_url}'):
            return self.driver.get(self.base_url)

    # Поиск элемента
    def is_element_present(self, how, what):
        try:
            with allure.step(f'Check element: type({how}), element({what})'):
                x = self.driver.find_element(how, what)
        except (NoSuchElementException):
            return False
        return x
