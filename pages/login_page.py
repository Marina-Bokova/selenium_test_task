from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        url_page = self.browser.current_url
        assert 'auth' in url_page, 'Failed to go to login page'
        assert self.element_is_present(*LoginPageLocators.SING_IN_BUTTON), 'Login page is not loaded'
