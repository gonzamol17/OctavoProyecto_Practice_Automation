import time
import pytest
import unittest
import HtmlTestRunner
from Utils import Utils as Utils
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.IframePage import IframePage
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))


@pytest.mark.usefixtures("test_setup")
class TestIframes(BaseClass):

    def test_Iframes(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        hp.closeCookiesWindows()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(1)
        hp.clickBtnIFrames()
        time.sleep(1)
        ifp = IframePage(driver)
        time.sleep(1)
        time.sleep(1)
        print(ifp.getTitle())
        driver.switch_to.frame(ifp.getIframeOne())
        time.sleep(1)
        ifp.selectSearchIcon()
        driver.execute_script("window.scrollTo(0, 150)")
        time.sleep(1)
        print("Elementos del Iframe 1:")
        ifp.getPopularSearchFristIframe()
        time.sleep(1)
        driver.switch_to.default_content()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 350)")
        time.sleep(1)
        driver.switch_to.frame(ifp.getIframeTwo())
        time.sleep(1)
        print("Elementos del Iframe 2:")
        ifp.getHeaderItemSecondIframe()
        time.sleep(1)










