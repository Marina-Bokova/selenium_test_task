import pytest

from pages.constants import TEXT_FOR_SEARCH_FIELD
from pages.main_page import MainPage
from pages.search_pages import YandexPage, GooglePage


@pytest.mark.parametrize('page_class', [
    pytest.param(YandexPage, marks=pytest.mark.xfail),  # May fail due to captcha issues
    GooglePage
])
def test_search_result_contains_sbermarketing_link(browser, page_class):
    page = page_class(browser)
    page.open()
    page.pass_captcha()
    page.perform_search(TEXT_FOR_SEARCH_FIELD)
    page.check_search_result()


@pytest.mark.xfail  # May fail due to captcha issues
def test_opening_of_sbermarketing_through_search_page(browser):
    page = YandexPage(browser)
    page.open()
    page.pass_captcha()
    page.perform_search(TEXT_FOR_SEARCH_FIELD)
    page.go_to_main_page()

    main_page = MainPage(browser, browser.current_url)
    main_page.should_be_main_page()
