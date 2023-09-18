from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE_INDICATOR = (By.XPATH, '//div[@data-anchor="anchor"]')
    COOKIE_BLOCK = (By.CSS_SELECTOR, '#cookie')
    COOKIE_BLOCK_CLOSE_BUTTON = (By.CSS_SELECTOR, "#cookie .modal__close")
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.header__mrm')
    PAGE_TITLE = (By.XPATH, '//head/title[contains(string(), "СберМаркетинг")]')


class LoginPageLocators:
    LOGIN_PAGE_INDICATOR = (By.XPATH, '//div[@data-anchor="anchor"]')
    SING_IN_BUTTON = (By.CSS_SELECTOR, '#saveButton')


class YandexPageLocators:
    CAPTCHA_BLOCK = (By.CSS_SELECTOR, '#root')
    CHECKBOX_CAPTCHA = (By.XPATH, '//div[contains(@class, "CheckboxCaptcha")]')
    SEARCH_FIELD = (By.XPATH, '//input[contains(@class, "search3__input")]')
    SEARCH_RESULT_TITLE = (By.XPATH, '//h2/span[contains(string(), "СберМаркетинг")]')
    SEARCH_RESULT_LINK = (By.XPATH, '//a[contains(@class, "Link")]/b[contains(string(), "SberMarketing.ru")]')


class GooglePageLocators:
    SEARCH_FIELD = (By.XPATH, '//form//textarea')
    SEARCH_RESULT_TITLE = (By.XPATH, '//h3[contains(string(), "СберМаркетинг – технологичный маркетинговый партнер")]')
    SEARCH_RESULT_LINK = (By.XPATH, '//cite[contains(string(), "https://sbermarketing.ru")]')
