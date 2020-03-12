import random
import allure
from selenium.webdriver.common.by import By
from tests.pages.BaseApp import BasePage


class ReviewLocators:
    REVIEW_BUTTON = (By.CSS_SELECTOR,
                     "div.object-view-reviews__body > div.object-view-reviews__panel.form.hidden-md.hidden-lg > a")
    REVIEW_WINDOW = (By.CSS_SELECTOR, "#new_review")
    REVIEW_TEXT = (By.CSS_SELECTOR, "#review_description")
    REVIEW_OWNER = (By.CSS_SELECTOR, "#review_owner_name")
    REVIEW_STAR = (By.CSS_SELECTOR, "div:nth-child(4)")
    REVIEW_SUBMIT = (By.CSS_SELECTOR, "#review-submit")
    REVIEW_BODY = (By.CSS_SELECTOR, ".review__body")
    REVIEW_TITLE = (By.CSS_SELECTOR, "div.review__title > span")


class ReviewPage(BasePage):
    def send_review_form(self):
        with allure.step('Генерируем коммент.'):
            text = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(10))
        with allure.step('Заполняем текст отзыва.'):
            self.is_element_present(*ReviewLocators.REVIEW_TEXT).send_keys(text)
        with allure.step('Заполняем имя.'):
            self.is_element_present(*ReviewLocators.REVIEW_OWNER).send_keys(text)
        with allure.step('Ставим 4 звезды отзыву.'):
            self.is_element_present(*ReviewLocators.REVIEW_STAR).click()
        with allure.step('Жмем принять.'):
            self.is_element_present(*ReviewLocators.REVIEW_SUBMIT).click()
        with allure.step('Сравниваем текст последнего отзыва с сгенерируемым текстом.'):
            body = self.is_element_present(*ReviewLocators.REVIEW_BODY).text
            title = self.is_element_present(*ReviewLocators.REVIEW_TITLE).text
            assert body == text == title, "Текст последнего отзыва не совпал с генерируемым текстом."
