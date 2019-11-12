import unittest
from selenium import webdriver
from time import sleep



class SearchTests(unittest.TestCase):

    def setUp(self):

        cd_url = '/Users/alexus/PycharmProjects/MyTestHRM/Drivers/chromedriver'
        browser = webdriver.Chrome(executable_path=cd_url)
        url = 'http://hrm-online.portnov.com'
        browser.get(url)
        self.browser = browser

    def tearDown(self):
        self.browser.quit()

    def test_search_by_name(self):
        browser = self.browser
        browser.find_element_by_id('txtUsername').send_keys('admin')
        browser.find_element_by_id('txtPassword').send_keys('password')
        browser.find_element_by_id('btnLogin').click()

        # search by name for 'James'
        browser.find_element_by_id('empsearch_employee_name_empName').click()
        browser.find_element_by_id('empsearch_employee_name_empName').clear()
        browser.find_element_by_id('empsearch_employee_name_empName').send_keys('James')
        browser.find_element_by_id('searchBtn').click()
        sleep(2)

        # get and count the results
        rows = browser.find_element_by_xpath('//tbody/tr')
        row_count = len(rows)

        # check that first result (first row) contains 'James'
        search_result = browser.find_element_by_xpath('//*[@id="resultTable"]/tbody/tr[1]/td[3]/a').text

        self.assertEqual(5, row_count)
        self.assertEqual('James', search_result)


my_suite = unittest.TestSuite()
my_suite.addTest(unittest.makeSuite())

if __name__ == '__main__':
    unittest.main()
