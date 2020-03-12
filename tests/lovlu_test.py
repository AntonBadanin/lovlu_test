import time
import pytest
import allure
from .pages.locators import LIST_PAGE, PLACE_LIST, MAIN_LINK
from .pages.LovluPages import ResponsePage


@allure.feature('Lovlu')
@allure.story('Основные разделы')
@allure.severity('critical')
@allure.link('https://task.leko.team/issues/21716', name='Ссылка на task.')
@allure.description("""Проверка работы основных разделов.""")
@pytest.mark.parametrize('add', LIST_PAGE)
def test_lovlu_main(browser, add):
    link = MAIN_LINK + add
    page = ResponsePage(browser, link)
    page.open()
    page.check_main()


@allure.feature('Lovlu')
@allure.story('Авторизация')
@allure.severity('critical')
@allure.link('https://task.leko.team/issues/21716', name='Ссылка на task.')
@allure.description("""Авторизация.""")
def test_autorization(browser):
    page = ResponsePage(browser, MAIN_LINK)
    page.open()
    page.autorization()
    time.sleep(1)
    page = ResponsePage(browser, MAIN_LINK + "my_places")
    page.open()
    page.check_profile()


@allure.feature('Lovlu')
@allure.story('Место рыбалки')
@allure.severity('normal')
@allure.link('https://task.leko.team/issues/21716', name='Ссылка на task.')
@allure.description("""Проверка места рыбалки.""")
@pytest.mark.parametrize('add', PLACE_LIST)
def test_place(browser, add):
    page = ResponsePage(browser, MAIN_LINK + "place/" + add)
    page.open()
    page.check_plase()
# Закоментил чтобы не создавалось много аккаунтов.
# def test_registration(browser):
#     page = ResponsePage(browser, MAIN_LINK)
#     page.open()
#     page.registration()
#     time.sleep(1)
#     page = ResponsePage(browser, MAIN_LINK + "my_places")
#     page.open()
#     page.check_profile()
