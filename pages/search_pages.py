import abc

from selenium.webdriver.common.keys import Keys

import pages.constants as c
from pages.base_page import BasePage
from pages.locators import YandexPageLocators, GooglePageLocators


class SearchPage(BasePage):
    PAGE_URL = ""

    def __init__(self, browser, timeout=c.TIMEOUT_IMPLICITLY_WAIT):
        super().__init__(browser, self.PAGE_URL, timeout)

    def _perform_search(self, text, locator):
        search_field = self.browser.find_element(*locator)
        search_field.clear()
        search_field.send_keys(text)
        search_field.send_keys(Keys.ENTER)

    @abc.abstractmethod
    def perform_search(self, text: str):
        return

    def pass_captcha(self):
        return

    def go_to_main_page(self):
        pass


class YandexPage(SearchPage):
    PAGE_URL = c.YANDEX_LINK

    def pass_captcha(self):
        if self.element_is_present(*YandexPageLocators.CAPTCHA_BLOCK):
            captcha_block = self.browser.find_element(*YandexPageLocators.CHECKBOX_CAPTCHA)
            captcha_block.click()

    def perform_search(self, text):
        self._perform_search(text, YandexPageLocators.SEARCH_FIELD)

    def check_search_result(self):
        assert self.element_is_present(*YandexPageLocators.SEARCH_RESULT_TITLE), 'The name is incorrect'
        assert self.element_is_present(*YandexPageLocators.SEARCH_RESULT_LINK), 'The link is missing or incorrect'

    def go_to_main_page(self):
        self.open_page_in_new_tab(YandexPageLocators.SEARCH_RESULT_TITLE, c.TITLE_MAIN_PAGE)


class GooglePage(SearchPage):
    PAGE_URL = c.GOOGLE_LINK

    def perform_search(self, text):
        self._perform_search(text, GooglePageLocators.SEARCH_FIELD)

    def check_search_result(self):
        assert self.element_is_present(*GooglePageLocators.SEARCH_RESULT_TITLE), 'The name is incorrect'
        search_link = self.browser.find_elements(*GooglePageLocators.SEARCH_RESULT_LINK)
        assert len(search_link) != 0, 'The link is missing or incorrect'
