import time
import pytest
import unittest
from Utils import Utils as Utils
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.WindowOperationsPage import WindowOperationsPage
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


class TestWindowOperationsReplacedOneTab(BaseClass):

    def test_WindowOperations_Replaced_OneTab(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        #hp.closeCookiesWindows()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 1200)")
        time.sleep(1)
        hp.clickBtnWindowOperations()
        wo = WindowOperationsPage(driver)
        original_url = wo.selectReplaceWindowButton()
        assert original_url == "https://automatenow.io/"
        time.sleep(2)









