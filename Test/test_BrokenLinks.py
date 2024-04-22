import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from Utils import Utils as Utils
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.BrokenLinksPage import BrokenLinksPage


class TestBrokenLinks(BaseClass):

    def test_BrokenLinks(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        #hp.closeCookiesWindows()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 2200)")
        time.sleep(1)
        hp.clickBtnBrokenLinks()
        time.sleep(1)
        bl = BrokenLinksPage(driver)
        url = bl.selectHyperlink()
        assert url == "https://practice-automation.com/broken-links/missing-page.html"
        print("El link está roto")
        time.sleep(2)











