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
from POM.CarouselsPage import CarouselsPage


@pytest.mark.usefixtures("test_setup")
class TestCarousels(BaseClass):

    def test_Carousels(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        hp.closeCookiesWindows()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(1)
        hp.clickBtnCarousels()
        time.sleep(1)
        cp = CarouselsPage(driver)
        time.sleep(1)
        cp.moveNextItem()
        time.sleep(1)
        cp.movePrevItem()
        time.sleep(2)











