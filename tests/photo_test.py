import allure
from .pages.PhotoPage import PhotoPage
from .pages.locators import MAIN_LINK


@allure.feature('Lovlu')
@allure.story('Фото')
@allure.severity('critical')
@allure.link('https://task.leko.team/issues/21716', name='Ссылка на task.')
@allure.description_html("""Проверка работоспособности фотослайдера.<br>Скрол фотослайдера у места рыбалки.""")
def test_photo(browser):
    page = PhotoPage(browser, MAIN_LINK + "place/lvovskie-prudy/")
    page.open()
    page.check_photo()
