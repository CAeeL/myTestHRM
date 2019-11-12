from . import BROWSER, CHROME_EXE_PATH, FIREFOX_EXE_PATH
from selenium import webdriver


def get_browser_session(browser_type=BROWSER):
    if browser_type.lower() == 'chrome':
        return webdriver.Chrome(executable_path=CHROME_EXE_PATH)
    elif browser_type.lower() == 'firefox':
        return webdriver.Firefox(executable_path=FIREFOX_EXE_PATH)
    else:
        raise NameError(f'The browser type {browser_type} is not supported at this time')


def get_screenshot_and_source(browser, file_name):

    # take a screenshot as .png file
    browser.get_screenshot_as_file(f'{file_name}.png')

    # source html file stored page_source
    file = open(f'{file_name}.html', 'w')
    file.write(browser.page_source)
    file.close()


def login(browser, username='admin', password='password'):
    browser.find_element_by_id('txtUsername').send_keys(username)
    browser.find_element_by_id('txtPassword').send_keys(password)
    browser.find_element_by_id('btnLogin').click()


def fill_in_field(browser, by, locator, text):
    browser.find_element(by, locator).clear()
    browser.find_element(by, locator).send_keys(text)




