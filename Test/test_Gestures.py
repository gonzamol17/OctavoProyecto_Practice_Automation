import time
import pytest
import unittest
import HtmlTestRunner
from Utils import Utils as Utils
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.GesturesPage import GesturesPage
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


@pytest.mark.usefixtures("test_setup")
class TestGestures(BaseClass):

    def test_Gestures(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        hp.closeCookiesWindows()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(1)
        hp.clickBtnGestures()
        time.sleep(1)
        gp = GesturesPage(driver)
        gp.moveTheBox()
        time.sleep(2)









