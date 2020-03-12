from selenium.webdriver.common.by import By

LIST_PAGE = ["place/belaya-dacha", "#signin", "about", "adverting", "cooperation", "rules", "feedback", "blog"]
PLACE_LIST = ["rybhoz-ramenskiy-gzhelka", "klyovoe-mesto"]
NAME = "Test"
MAIL = "1@leko.team"
PASSWORD = "123456"
MAIN_LINK = "https://lovlu.ru.dev.leko.team/"


class RegionLocators:
    REGION_DESRIPTION = (By.CSS_SELECTOR, ".location-desc")
    ALTAY = ["body > main > section.container.regions > div:nth-child(2) > p:nth-child(1) > a", "altajskij-kraj"]
    ASTRACHAN = ["body > main > section.container.regions > div:nth-child(2) > p:nth-child(2) > a",
                 "astrahanskaya-oblast"]
    BRIANSK = ["body > main > section.container.regions > div:nth-child(2) > p:nth-child(3) > a", "bryanskaya-oblast"]


class ColorLocators:
    SEARCH_BUTTON = {'css': '.button.button--search', 'color': '#ed465d', 'size': {'height': 36, 'width': 36}}


class LovluMainLocators:
    HEADER_LOGO = (By.CSS_SELECTOR, ".logo.link-naked")
    FOOTER = (By.CSS_SELECTOR, ".footer")
    MAIN_NAVIGATION = (By.CSS_SELECTOR, ".main-navigation")
    ERROR_404 = (By.CSS_SELECTOR, ".is-errors-error404")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, ".button.button--danger.site-signup.popup-anchor123")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#signup")
    REGISTRATION_NAME = (By.CSS_SELECTOR, "#user_setting_user_attributes_name")
    REGISTRATION_SURNAME = (By.CSS_SELECTOR, "#user_setting_user_attributes_surname")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, ".string.email.required.form__input-field")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, ".password.required.form__input-field")
    REGISTRATION_BUTTON_SUBMIT = (By.CSS_SELECTOR, ".btn.button.button--large.button--danger.form__submit")
    PROFILE_NAME = (By.CSS_SELECTOR, ".profile__username")
    AUTORIZTION_FORM = (By.CSS_SELECTOR, "#signin")
    AUTORIZTION_BUTTON = (By.CSS_SELECTOR, ".site-signin.popup-anchor")
    BEST_PLACE = (By.CSS_SELECTOR, ".link-black.thumbnail__name")
    BEST_PLACE_COUNTER = (By.CSS_SELECTOR, ".counter__num.counter--small")


class LovluPlaceLocators:
    PHOTO_PROFILE = (By.CSS_SELECTOR, ".gallery.lightbox-gallery.pointer")
    SOCIAL = (By.CSS_SELECTOR, ".socials.socials--small.socials--solid.socials--type-inline.object-view__socials")
    CONDICTIONS = (By.CSS_SELECTOR, ".object-view__description-row.object-view__description-row--conditions")
    PRICE_PLACE = (By.CSS_SELECTOR, ".object-view__description-row.object-view__description-row--prices")
    DECRIPTION = (By.CSS_SELECTOR, ".indent")
    DECRIPTION_FISH = (By.CSS_SELECTOR, ".object-view__description-text.object-view__description-text--wide")
    REVIEWS = (By.CSS_SELECTOR, ".object-view-reviews__inner")
    MAPS = (By.CSS_SELECTOR, ".ymaps-2-1-75-events-pane.ymaps-2-1-75-user-selection-none")
    VIEWS_LOCATION = (By.CSS_SELECTOR, ".object-view-location")
    BREADCRUMBS = (By.CSS_SELECTOR, ".breadcrumbs")
    ANCHOR = (By.CSS_SELECTOR, "body > main > div.object > section:nth-child(1) > div:nth-child(2) > div > "
                               "section > div.object-view__container > div.object-view__dashboard.js-is-clone > "
                               "div.dashboard > div.dashboard__header > a")
    ANCHOR1 = (By.CSS_SELECTOR, ".button__label")
    ADD_FAVORITES = (By.CSS_SELECTOR, ".button__inner")