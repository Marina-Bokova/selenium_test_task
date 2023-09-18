from pages.base_page import BasePage
from pages.constants import MAIN_PAGE_LINK, TITLE_LOGIN_PAGE
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def should_be_main_page(self):
        url_page = self.browser.current_url
        assert MAIN_PAGE_LINK in url_page, 'Failed to go to main page'
        assert self.element_is_present(*MainPageLocators.PAGE_TITLE), 'Failed to go to main page'

    def close_cookie_block(self):
        if self.element_is_present(*MainPageLocators.COOKIE_BLOCK):
            cookie_block_close = self.browser.find_element(*MainPageLocators.COOKIE_BLOCK_CLOSE_BUTTON)
            cookie_block_close.click()

    def should_be_login_button(self):
        assert self.element_is_present(*MainPageLocators.LOGIN_BUTTON), 'Button "Вход в MRM" is not presented'

    def go_to_login_page_and_switch_to_new_tab(self):
        self.open_page_in_new_tab(MainPageLocators.LOGIN_BUTTON, TITLE_LOGIN_PAGE)
