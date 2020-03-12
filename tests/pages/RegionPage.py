import allure
from selenium.webdriver.common.by import By
from tests.pages.BaseApp import BasePage
from tests.pages.locators import LovluPlaceLocators, LovluMainLocators


class LocationLocators:
    LOCATION_NAME = (By.CSS_SELECTOR, ".location-name__inner")
    LOCATION_DESC = (By.CSS_SELECTOR, ".location-desc")
    LOCATION_MAP = (By.CSS_SELECTOR, ".location-map__inner")
    LOCATION_PLACE = (By.CSS_SELECTOR, ".location-places")
    LOCATION_REGION = (By.CSS_SELECTOR, ".container.regions")


class RegionPage(BasePage):
    def check_region_element(self):
        with allure.step('Проверяем наличие основных элементов.'):
            assert self.is_element_present(*LocationLocators.LOCATION_NAME), "НЕ ВИДНО LOCATION_NAME"
            assert self.is_element_present(*LocationLocators.LOCATION_DESC), "НЕ ВИДНО LOCATION_DESC"
            assert self.is_element_present(*LocationLocators.LOCATION_MAP), "НЕ ВИДНО LOCATION_MAP"
            assert self.is_element_present(*LocationLocators.LOCATION_PLACE), "НЕ ВИДНО LOCATION_PLACE"
            assert self.is_element_present(*LocationLocators.LOCATION_REGION), "НЕ ВИДНО LOCATION_REGION"
        with allure.step('Кликаем на добавить в избранное и проверяем наличие формы авторизации.'):
            self.is_element_present(*LovluPlaceLocators.ADD_FAVORITES).click()
            assert self.is_element_present(*LovluMainLocators.REGISTRATION_FORM), "Не видно ворму регистрации"
