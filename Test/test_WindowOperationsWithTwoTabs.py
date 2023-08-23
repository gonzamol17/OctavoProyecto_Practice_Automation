import time
import pytest
import unittest
import HtmlTestRunner
from Utils import Utils as Utils
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.WindowOperationsPage import WindowOperationsPage
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


@pytest.mark.usefixtures("test_setup")
class TestWindowOperationsWithTwoTabs(BaseClass):

    def test_WindowOperations_With_TwoTabs(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        hp.closeCookiesWindows()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(1)
        hp.clickBtnWindowOperations()
        wo = WindowOperationsPage(driver)
        parenturl = wo.selectNewTabButton()
        assert parenturl == "https://practice-automation.com/window-operations/"
        time.sleep(2)









