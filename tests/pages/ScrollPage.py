import time
from selenium.webdriver.common.by import By
from tests.pages.BaseApp import BasePage


class ScrollLocators:
    FEEDBACK_LINE = (By.CSS_SELECTOR, ".owl-stage")
    FEEDBACK_CENTER = (By.CSS_SELECTOR, ".owl-item.active.center")
    FEEDBACK_CENTER_TEXT = (By.CSS_SELECTOR, ".owl-item.active.center .feedback__title.link-black")
    FEEDBACK_PREV_BUTTON = (By.CSS_SELECTOR, ".owl-prev")
    FEEDBACK_NEXT_BUTTON = (By.CSS_SELECTOR, ".owl-next")


class ScrollPage(BasePage):
    def check_scroll(self):
        expected = self.driver.find_element(*ScrollLocators.FEEDBACK_LINE).value_of_css_property('transform')
        self.is_element_present(*ScrollLocators.FEEDBACK_NEXT_BUTTON).click()
        time.sleep(0.5)
        received = self.driver.find_element(*ScrollLocators.FEEDBACK_LINE).value_of_css_property('transform')
        assert expected != received, f"{expected} == {received}"
        self.is_element_present(*ScrollLocators.FEEDBACK_PREV_BUTTON).click()
        time.sleep(0.5)
        last = self.is_element_present(*ScrollLocators.FEEDBACK_LINE).value_of_css_property('transform')
        assert last != received and last == expected, f"{last} == {received}"
