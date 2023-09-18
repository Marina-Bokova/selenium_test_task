from pages.constants import MAIN_PAGE_LINK
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MAIN_PAGE_LINK)
    page.open()
    page.close_cookie_block()
    page.should_be_login_button()
    page.go_to_login_page_and_switch_to_new_tab()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
