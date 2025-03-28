import pytest

from utils.common import initiate_webdriver

driver=None
@pytest.fixture()
def initiate_driver():
     global driver
     driver=initiate_webdriver()
     print("driver initITA")