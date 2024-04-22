import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from Utils import Utils as Utils
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.ClickEventsPage import ClickEventsPage


class TestClickEvents(BaseClass):

    def test_Click_Events(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        #hp.closeCookiesWindows()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 1500)")
        time.sleep(1)
        hp.clickBtnClickEvents()
        ce = ClickEventsPage(driver)
        cat = ce.selectBtnCat()
        assert cat == "Meow!"
        time.sleep(1)
        dog = ce.selectBtnDog()
        assert dog == "Woof!"
        time.sleep(1)
        pig = ce.selectBtnPig()
        assert pig == "Oink!"
        time.sleep(1)
        cow = ce.selectBtnCow()
        assert cow == "Moo!"
        time.sleep(2)










