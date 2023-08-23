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
from POM.TablesPage import TablesPage


@pytest.mark.usefixtures("test_setup")
class TestFoundValueIntoTables(BaseClass):

    def test_Found_A_Value_Into_Tables(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        hp.closeCookiesWindows()
        time.sleep(1)
        hp.clickBtnTables()
        tp = TablesPage(driver)
        item = "Laptop"
        product = tp.searchAValueIntoAFromTables(item)
        assert product == item
        time.sleep(2)









