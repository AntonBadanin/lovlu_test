import allure
from .pages.NewsPage import NewsPage


@allure.feature('Lovlu')
@allure.story('develop')
@allure.severity('critical')
@allure.link('https://task.leko.team/issues/21716', name='Ссылка на task.')
@allure.description_html("""Проверка работоспособности раздела новости.<br> Тест на проходит на боевой в данный
момент""")
def test_news(browser):
    page = NewsPage(browser, "https://lovlu.ru/place/marlin/news")
    page.open()
    page.check_button_list()
    page.go_to_news()
