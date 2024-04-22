import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from Utils import Utils as Utils
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.BrokenImagesPage import BrokenImagesPage


class TestBrokenImages(BaseClass):

    def test_BrokenImages(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        #hp.closeCookiesWindows()
        driver.execute_script("window.scrollTo(0, 2200)")
        time.sleep(1)
        hp.clickBtnBrokenImages()
        bp = BrokenImagesPage(driver)
        aux = bp.getAllImages()
        assert aux == 1
        time.sleep(2)











