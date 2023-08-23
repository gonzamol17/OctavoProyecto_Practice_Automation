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
from POM.AccordionsPage import AccordionsPage


@pytest.mark.usefixtures("test_setup")
class TestAccordions(BaseClass):

    def test_Accordions(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        hp.closeCookiesWindows()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(1)
        hp.clickBtnAccordions()
        ap = AccordionsPage(driver)
        time.sleep(1)
        ap.selectAccordion()
        time.sleep(1)
        assert ap.getTitleFromAccordion() == "This is an accordion item."
        time.sleep(2)











