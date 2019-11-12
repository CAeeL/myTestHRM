import os
import unittest

from selenium.webdriver.support.wait import WebDriverWait

from .utils import get_browser_session, get_screenshot_and_source, login
from . import BASE_URL


class BaseTestFixture(unittest.TestCase):
    def setUp(self):
        browser = get_browser_session()
        browser.get(BASE_URL)
        browser.maximize_window()
        browser.delete_all_cookies()

        self.browser = browser
        self.wait = WebDriverWait(browser, 5)

    def tearDown(self) -> None:
        if self._outcome.errors[1][1] is not None:
            folder_name = 'results'
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
            get_screenshot_and_source(self.browser, folder_name + '/' + self._testMethodName)

        self.browser.quit()
