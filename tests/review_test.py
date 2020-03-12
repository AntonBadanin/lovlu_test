import allure
from .pages.ReviewPage import ReviewPage
from .pages.locators import MAIN_LINK


@allure.feature('Lovlu')
@allure.story('Отзывы')
@allure.severity('critical')
@allure.link('https://task.leko.team/issues/21716', name='Ссылка на task.')
@allure.description_html("""Проверка работоспособности отзывов.<br>
 Так есть проверка отображение нового отзыва на главной.""")
def test_check_review(browser):
    page = ReviewPage(browser, MAIN_LINK + "/place/lvovskie-prudy/review/new")
    page.open()
    page.send_review_form()
