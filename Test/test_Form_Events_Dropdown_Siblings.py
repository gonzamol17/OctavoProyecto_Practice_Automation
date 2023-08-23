import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import HtmlTestRunner
from Utils import Utils as Utils
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.FormEventsPage import FormEventsPage


@pytest.mark.usefixtures("test_setup")
class TestFormEventsSelectDropdown(BaseClass):

    def test_FormEvents_Select_Dropdown(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        hp.closeCookiesWindows()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 150)")
        time.sleep(1)
        hp.clickBtnFormEvents()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(1)
        fe = FormEventsPage(driver)
        option = "Yes"
        fe.chooseOneOptionFromDropdown(option)
        assert fe.verifyValueInDropdown() == option
        time.sleep(2)










