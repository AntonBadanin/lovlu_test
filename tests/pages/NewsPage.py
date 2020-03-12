import allure
from selenium.webdriver.common.by import By
from tests.pages.BaseApp import BasePage


class NewsLocators:
    NEXT_TEN_NEWS = (By.CSS_SELECTOR, ".button.button--default.load-event")
    BLOCK11_NEWS = (By.CSS_SELECTOR, "div.posts-list > div:nth-child(11)")
    BLOCK12_NEWS = (By.CSS_SELECTOR, "div.posts-list > div:nth-child(12)")
    BLOCK1_NEWS = (By.CSS_SELECTOR, "div.posts-list > div:nth-child(1)")
    TITLE1_NEWS = (By.CSS_SELECTOR, ".posts-list__title")
    H2 = (By.CSS_SELECTOR, ".h2")
    H5 = (By.CSS_SELECTOR, ".h5")
    DATE1 = (By.CSS_SELECTOR, ".div.posts-list__header > div > div > span")
    DATE2 = (By.CSS_SELECTOR, ".news__pubdate")


class NewsPage(BasePage):
    def check_button_list(self):
        with allure.step('Проверяем наличие 11 блока и отсутсвие 12 блока.'):
            assert self.is_element_present(*NewsLocators.BLOCK11_NEWS), "Не видно 11 блока"
            assert not self.is_element_present(*NewsLocators.BLOCK12_NEWS), "Видно 12 блок"
        with allure.step('Кликаем на предыдущие новости.'):
            self.is_element_present(*NewsLocators.NEXT_TEN_NEWS).click()
        with allure.step('Проверяем наличие 12 блока.'):
            assert self.is_element_present(*NewsLocators.BLOCK12_NEWS), "Не видно 12 блок"

    def go_to_news(self):
        with allure.step('Кликаем по за головку 1 новости.'):
            title1 = self.is_element_present(*NewsLocators.H5).text
            self.is_element_present(*NewsLocators.H5).click()
        with allure.step('Сравниваем совпадение заголовков.'):
            title2 = self.is_element_present(*NewsLocators.H2).text
            assert title1 == title2, f"Не совпадают заголовоки."
