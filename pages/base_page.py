from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.constants import TIMEOUT_IMPLICITLY_WAIT, TIMEOUT_EXPLICITLY_WAIT


class BasePage:
    def __init__(self, browser, url, timeout=TIMEOUT_IMPLICITLY_WAIT):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.wait = WebDriverWait(self.browser, TIMEOUT_EXPLICITLY_WAIT)

    def open(self):
        self.browser.get(self.url)

    def element_is_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def open_page_in_new_tab(self, locator, page_title):
        current_window = self.browser.current_window_handle
        assert len(self.browser.window_handles) == 1, 'More than one tab open'
        button = self.browser.find_element(*locator)
        button.click()
        self.wait.until(EC.number_of_windows_to_be(2))
        for window_handle in self.browser.window_handles:
            if window_handle != current_window:
                self.browser.switch_to.window(window_handle)
                break
        self.wait.until(EC.title_is(page_title))
