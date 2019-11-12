import unittest
from time import sleep
from selenium import webdriver
from lib.utils import login
from lib.sup_tdown import BaseTestFixture


class MyTestCase(BaseTestFixture):

    def test_valid_login(self):


        login(browser=browser)
        welcome_message = browser.find_element_by_id('welcome').text
        self.assertEqual('Welcome Admin', welcome_message)

    def test_something(self):
        pass






if __name__ == '__main__':
    unittest.main()
