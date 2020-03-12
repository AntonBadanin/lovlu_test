# import pytest
# from allure_commons.types import AttachmentType  # Не удалять!!!
# import allure
#
# from .pages.BaseApp import BasePage
# from .pages.locators import LIST_PAGE, PLACE_LIST, MAIN_LINK, ColorLocators
# from .pages.LovluPages import ResponsePage
#
#
# # Проверка цвета
# @allure.feature('Lovlu')
# @allure.story('Основные разделы')
# @allure.severity('critical')
# @allure.link('https://task.leko.team/issues/21716', name='Ссылка на task.')
# @allure.description("""Проверка работы основных разделов.""")
# def test_lovlu_main(browser):
#     link = MAIN_LINK
#     page = ResponsePage(browser, link)
#     page.open()
#     page.check_background_color(sel=ColorLocators.SEARCH_BUTTON)
#
#
# # Проверка размера
# @allure.link('https://www.ru')
# def test_bileti(browser, baseurl, token):
#     page = ResponsePage(browser, "https://lovlu.ru.dev.leko.team/")
#     page.open()
#     page.check_size(css=ColorLocators.SEARCH_BUTTON)
#     page.check_background_color(css=ColorLocators.SEARCH_BUTTON)
#
#
# @allure.link('https://www.ru')
# @allure.step('Ещё один тест')
# def test_bileti(browser, baseurl, token):
#     page = ResponsePage(browser, "https://lovlu.ru.dev.leko.team/")
#     page.open()
