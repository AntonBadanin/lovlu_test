import allure
from selenium.webdriver.common.by import By
from tests.pages.BaseApp import BasePage


class AutofillLocators:
    MAINFIELD = (By.NAME, "query")
    AUTOFILLFIELD = (By.ID, "ui-id-1")
    AUTOFILLFIELD_1 = (By.CSS_SELECTOR, "#ui-id-1 > li:nth-child(1)")
    AUTOFILLFIELD_2 = (By.CSS_SELECTOR, "#ui-id-1 > li:nth-child(2)")
    AUTOFILLFIELD_3 = (By.CSS_SELECTOR, "#ui-id-1 > li:nth-child(3)")


class AutofillPage(BasePage):
    def check_autofill(self):
        self.is_element_present(*AutofillLocators.MAINFIELD).send_keys("Москва")
        self.is_element_present(*AutofillLocators.AUTOFILLFIELD)
        text_expected = ["платный пруд Москва", "Москва, Россия",
                         "Московский международный деловой центр Москва-Сити, Пресненский район, Центральный "
                         "административный округ, Москва, Россия"]
        text_received_1 = self.driver.find_element(*AutofillLocators.AUTOFILLFIELD_1).text
        text_received_2 = self.driver.find_element(*AutofillLocators.AUTOFILLFIELD_2).text
        text_received_3 = self.driver.find_element(*AutofillLocators.AUTOFILLFIELD_3).text
        with allure.step('Проверяем текст автозаполнения'):
            assert text_expected[0] == text_received_1, f"{text_expected[0]} =! {text_received_1}"
            assert text_expected[1] == text_received_2, f"{text_expected[1]} =! {text_received_2}"
            assert text_expected[2] == text_received_3, f"{text_expected[2]} =! {text_received_3}"
