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


class TestGetallRecordsFromTables(BaseClass):

    def test_Get_All_Records_From_Tables(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        #hp.closeCookiesWindows()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 900)")
        time.sleep(1)
        hp.clickBtnTables()
        tp = TablesPage(driver)
        tp.showAllElementsFromTables()
        time.sleep(2)









