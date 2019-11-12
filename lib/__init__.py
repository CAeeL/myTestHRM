import os

#______________________________Precondition Steps_______________________________

BROWSER = 'chrome'

TEST_DIR = os.path.dirname(os.path.abspath(__file__))

_file_ext = ''              # no file extension for mac
if os.name == 'nt':         # os.name == 'posix' for mac
    _file_ext = '.exe'


CHROME_EXE_PATH = f'{TEST_DIR}/../Drivers/chromedriver{_file_ext}'
FIREFOX_EXE_PATH = f'{TEST_DIR}/../Drivers/geckodriver{_file_ext}'

BASE_URL = 'http://hrm-online.portnov.com'
