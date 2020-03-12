import allure
from .pages.AutoFillPage import AutofillPage
from .pages.RegionPage import RegionPage
from .pages.ScrollPage import ScrollPage
from .pages.locators import MAIN_LINK, RegionLocators
from .pages.LovluPages import ResponsePage


@allure.feature('Lovlu')
@allure.story('Основные разделы')
@allure.severity('critical')
@allure.link('https://task.leko.team/issues/21716', name='Ссылка на task.')
@allure.description("""Проверка ссылок на регионы.""")
def test_region_url(browser):
    page = ResponsePage(browser, MAIN_LINK)
    page.open()
    page.check_region(css=RegionLocators.ALTAY)
    page.check_region(css=RegionLocators.ASTRACHAN)
    page.check_region(css=RegionLocators.BRIANSK)


@allure.feature('Lovlu')
@allure.story('Основные разделы')
@allure.severity('critical')
@allure.link('https://task.leko.team/issues/21716', name='Ссылка на task.')
@allure.description("""Проверка ссылок на лучшие места.""")
def test_best_plase(browser):
    page = ResponsePage(browser, MAIN_LINK)
    page.open()
    page.check_best_place_url()


@allure.feature('Lovlu')
@allure.story('Основные разделы')
@allure.severity('critical')
@allure.link('https://task.leko.team/issues/21716', name='Ссылка на task.')
@allure.description("""Проверка страницы региона.""")
def test_region_element(browser):
    page = RegionPage(browser, MAIN_LINK + "altajskij-kraj")
    page.open()
    page.check_region_element()


@allure.feature('Lovlu')
@allure.story('Основные разделы')
@allure.severity('critical')
@allure.link('https://task.leko.team/issues/21716', name='Ссылка на task.')
@allure.description("""Проверка автозаполнения.""")
def test_autofill(browser):
    page = AutofillPage(browser, MAIN_LINK)
    page.open()
    page.check_autofill()


@allure.feature('Lovlu')
@allure.story('Основные разделы')
@allure.severity('critical')
@allure.link('https://task.leko.team/issues/21716', name='Ссылка на task.')
@allure.description("""Проверка скролла.""")
def test_scroll(browser):
    page = ScrollPage(browser, MAIN_LINK)
    page.open()
    page.check_scroll()


@allure.feature('Lovlu')
@allure.story('Основные разделы')
@allure.severity('critical')
@allure.link('https://task.leko.team/issues/21716', name='Ссылка на task.')
@allure.description("""Проверка ссылки на соц.сети.""")
def test_social(browser):
    page = ScrollPage(browser, MAIN_LINK)
    page.open()
    page.check_scroll()
