import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from Utils import Utils as Utils
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.AdsPage import AdsPage


class TestExplicitWaitAds(BaseClass):

    def test_Explicit_Wait_Ads(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        #hp.closeCookiesWindows()
        driver.execute_script("window.scrollTo(0, 1500)")
        time.sleep(1)
        hp.clickBtnAds()
        ads = AdsPage(driver)
        title = ads.verifyPopUpIsPresented()
        assert "Please make sure" in title
        print("Ahora se está visualizando el texto correcto¡¡¡¡¡")
        time.sleep(2)










