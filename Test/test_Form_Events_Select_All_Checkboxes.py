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
class TestFormEventsSelectAllCheckboxes(BaseClass):

    def test_FormEvents_Select_All_Checkboxes(self):
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
        fe = FormEventsPage(driver)
        time.sleep(1)
        status = fe.selectAllItems()
        flag = 0
        res = all(i for i in status)
        assert res is True
        print("Is List completely True ? : " + str(res))
        time.sleep(2)










