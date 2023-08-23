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
from POM.AdsPage import AdsPage


@pytest.mark.usefixtures("test_setup")
class TestExplicitWaitAds(BaseClass):

    def test_Explicit_Wait_Ads(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        hp.closeCookiesWindows()
        time.sleep(1)
        hp.clickBtnAds()
        ads = AdsPage(driver)
        text = ads.verifyPopUpIsPresented()
        assert "will appear" in text
        print("Ahora se está visualizando el texto correcto¡¡¡¡¡")
        time.sleep(2)










