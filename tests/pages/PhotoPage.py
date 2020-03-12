import time
import allure
from selenium.webdriver.common.by import By
from tests.pages.BaseApp import BasePage


class PhotoLocators:
    PHOTO_MAIN = (By.CSS_SELECTOR, ".gallery__holder")
    PHOTO_SLIDER = (By.CSS_SELECTOR, ".lg-thumb-outer.lg-grab")
    PHOTO_NEXT = (By.CSS_SELECTOR, ".lg-next.lg-icon")
    PHOTO_PREV = (By.CSS_SELECTOR, ".lg-prev.lg-icon")


class PhotoPage(BasePage):
    def check_photo(self):
        with allure.step('Кликаем на главное фото.'):
            self.is_element_present(*PhotoLocators.PHOTO_MAIN).click()
        with allure.step('Проверяем наличие слайдера снизу.'):
            assert self.is_element_present(*PhotoLocators.PHOTO_SLIDER), "Нету слайдера"
            current_url = self.driver.current_url
        with allure.step('Кликаем на кнопку следующее фото.'):
            self.is_element_present(*PhotoLocators.PHOTO_NEXT).click()
            time.sleep(1)
            next_url = self.driver.current_url
        with allure.step('Сравниваем изменился ли url после клика.'):
            assert current_url != next_url, f"URL страниц совпали.  {next_url}"
        with allure.step('Кликаем на кнопку предыдущее фото.'):
            self.is_element_present(*PhotoLocators.PHOTO_PREV).click()
            time.sleep(1)
            prev_url = self.driver.current_url
        with allure.step('Сравниваем изменился ли url после клика. Так же url должен совпадать с первоначальным.'):
            assert prev_url != next_url and prev_url == current_url, f"Ошибка при проверки URL."
