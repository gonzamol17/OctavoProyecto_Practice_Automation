import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from Utils import Utils as Utils
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.TablesPage import TablesPage


class TestFoundValueIntoTables(BaseClass):

    def test_Found_A_Value_Into_Tables(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        #hp.closeCookiesWindows()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 800)")
        time.sleep(2)
        hp.clickBtnTables()
        tp = TablesPage(driver)
        item = "Laptop"
        product = tp.searchAValueIntoAFromTables(item)
        assert product == item
        time.sleep(2)









