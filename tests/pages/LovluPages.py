import ast
import allure
from selenium.webdriver.common.by import By
from tests.pages.BaseApp import BasePage
from .locators import LovluMainLocators, LovluPlaceLocators, MAIL, PASSWORD, NAME, RegionLocators, MAIN_LINK


class ResponsePage(BasePage):
    # Проверка основных разделов
    def check_main(self):
        with allure.step('Проверяем наличие основных элементов.'):
            assert self.is_element_present(*LovluMainLocators.FOOTER), "НЕ ВИДНО FOOTER"
            assert self.is_element_present(*LovluMainLocators.MAIN_NAVIGATION), "НЕ ВИДНО MAIN_NAVIGATION"
            assert self.is_element_present(*LovluMainLocators.HEADER_LOGO), "НЕ ВИДНО HEADER_LOGO"
        with allure.step('Проверяем отсутсвие 404 ошибки.'):
            assert not self.is_element_present(*LovluMainLocators.ERROR_404), "ВИДНО ERROR_404"

    # Регистрация
    def registration(self):
        self.driver.find_element(*LovluMainLocators.REGISTRATION_BUTTON).click()
        assert self.is_element_present(*LovluMainLocators.REGISTRATION_FORM), "НЕ ВИДНО REGISTRATION_FORM"
        self.driver.find_element(*LovluMainLocators.REGISTRATION_NAME).send_keys(NAME)
        self.driver.find_element(*LovluMainLocators.REGISTRATION_SURNAME).send_keys(NAME)
        self.driver.find_element(*LovluMainLocators.REGISTRATION_EMAIL).send_keys(MAIL)
        self.driver.find_element(*LovluMainLocators.REGISTRATION_PASSWORD).send_keys(PASSWORD)
        self.driver.find_element(*LovluMainLocators.REGISTRATION_BUTTON_SUBMIT).click()

    # Проверка места рыбалки
    def check_plase(self):
        with allure.step('Проверяем наличие основных элементов.'):
            assert self.is_element_present(*LovluPlaceLocators.PHOTO_PROFILE), "НЕ ВИДНО PHOTO_PROFILE"
            assert self.is_element_present(*LovluPlaceLocators.SOCIAL), "НЕ ВИДНО SOCIAL"
            assert self.is_element_present(*LovluPlaceLocators.CONDICTIONS), "НЕ ВИДНО CONDICTIONS"
            assert self.is_element_present(*LovluPlaceLocators.PRICE_PLACE), "НЕ ВИДНО PRICE_PLACE"
            assert self.is_element_present(*LovluPlaceLocators.DECRIPTION), "НЕ ВИДНО DECRIPTION"
            assert self.is_element_present(*LovluPlaceLocators.DECRIPTION_FISH), "НЕ ВИДНО DECRIPTION_FISH"
            assert self.is_element_present(*LovluPlaceLocators.REVIEWS), "НЕ ВИДНО REVIEWS"
            assert self.is_element_present(*LovluPlaceLocators.MAPS), "НЕ ВИДНО MAPS"
            assert self.is_element_present(*LovluPlaceLocators.VIEWS_LOCATION), "НЕ ВИДНО VIEWS_LOCATION"
            assert self.is_element_present(*LovluPlaceLocators.BREADCRUMBS), "НЕ ВИДНО BREADCRUMBS"
        with allure.step('Нажимаем на якорь и проверяем наличие формы авторизации.'):
            self.is_element_present(*LovluPlaceLocators.ANCHOR1).click()
            assert self.is_element_present(*LovluMainLocators.AUTORIZTION_FORM), "НЕ ВИДНО АВТОРИЗАЦИИ"

    # Проверка профился после авторизации
    def check_profile(self):
        assert not self.is_element_present(*LovluMainLocators.ERROR_404), "ВИДНО ERROR_404"
        assert self.is_element_present(*LovluMainLocators.PROFILE_NAME), "НЕ ВИДНО PROFILE_NAME"

    # Авторизация
    def autorization(self):
        with allure.step('Нажимаем на кнопку авторизации.'):
            self.is_element_present(*LovluMainLocators.AUTORIZTION_BUTTON).click()
        assert self.is_element_present(*LovluMainLocators.AUTORIZTION_FORM), "НЕ ВИДНО AUTORIZTION_FORM"
        with allure.step('Заполняем почту.'):
            self.is_element_present(*LovluMainLocators.REGISTRATION_EMAIL).send_keys(MAIL)
        with allure.step('Заполняем пароль.'):
            self.is_element_present(*LovluMainLocators.REGISTRATION_PASSWORD).send_keys(PASSWORD)
        with allure.step('Нажимаем Войти.'):
            self.is_element_present(*LovluMainLocators.REGISTRATION_BUTTON_SUBMIT).click()

    # Проверка цвета фона элемента
    def check_background_color(self, css):
        rgba = self.driver.find_element(By.CSS_SELECTOR, css['css']).value_of_css_property('background-color')
        r, g, b, alpha = ast.literal_eval(rgba.strip("rgba"))
        x = '#%02x%02x%02x' % (r, g, b)
        with allure.step('Проверяем цвет элемента.'):
            assert x == css['color'], f"У селектора {css['css']} цвет должен быть {css['color']}, сейчас он {x}"

    def check_size(self, css):
        x = self.driver.find_element(By.CSS_SELECTOR, css['css'])
        with allure.step('Проверяем размер элемента.'):
            assert x.size == css['size'], f"Размер {css['css']} равен {x.size},а должен {css['size']}"

    def check_region(self, css, ):
        with allure.step(f'Кликаем по {css[0]}'):
            self.driver.find_element(By.CSS_SELECTOR, css[0]).click()
        x = self.driver.current_url
        assert self.is_element_present(*RegionLocators.REGION_DESRIPTION), "НЕ ВИДНО REGION_DESRIPTION"
        with allure.step('Проверяем текущий url'):
            assert x == MAIN_LINK + css[1], \
                f"Текущий url: {x} . Ожидаемый url: {MAIN_LINK + css[1]}"

    def check_best_place_url(self):
        title_expected = self.driver.find_element(*LovluMainLocators.BEST_PLACE).text
        self.driver.find_element(*LovluMainLocators.BEST_PLACE).click()
        title_received = self.driver.find_element(By.CSS_SELECTOR, '.h1').text
        with allure.step('Проверка совпадения текста: элемент на главной и страница места'):
            assert title_expected == title_received, f"Название не совпадает с текстом элемента."


