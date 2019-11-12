import unittest
import random
from selenium import webdriver
from lib import BASE_URL
from lib.sup_tdown import BaseTestFixture
from lib.utils import get_browser_session


class MyCalculatorTestCase(BaseTestFixture):

    BASE_URL = 'http://www.math.com/students/calculators/source/basic.htm'


    def test_basic_addition(self):
        browser = self.browser
        num1, num2 = random.randint(0, 9), random.randint(0, 9)




if __name__ == '__main__':
    unittest.main()
