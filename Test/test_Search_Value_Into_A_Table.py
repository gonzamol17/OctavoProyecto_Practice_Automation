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
class TestSearchValueIntoTable(BaseClass):

    def test_Search_A_Value_Into_Table(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        hp.closeCookiesWindows()
        time.sleep(1)
        hp.clickBtnTables()
        tp = TablesPage(driver)
        driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(2)
        country = "United States"
        countries = tp.searchACountryFromTables(country)
        print(countries)
        assert country in countries
        time.sleep(2)









