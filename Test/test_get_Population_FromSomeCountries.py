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
class TestGetPopulationFromCountries(BaseClass):

    def test_Get_Population_From_Countries(self):
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
        numberofselector = tp.showNumberFromSelector()
        numberofpagination = tp.showNumberFromPagination()
        assert numberofselector in numberofpagination
        country1 = "India"
        country2 = "United States"
        totPopulation = tp.searchTwoCountryRecordAndGetPopulation(country1, country2)
        print("\nLa población total entre "+str(country1)+" y "+str(country2)+" es: ")
        print(totPopulation)
        time.sleep(2)









