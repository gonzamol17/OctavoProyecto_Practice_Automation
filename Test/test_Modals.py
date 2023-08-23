import time
import pytest
import unittest
import HtmlTestRunner
from Utils import Utils as Utils
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.ModalsPage import ModalsPage
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))


@pytest.mark.usefixtures("test_setup")
class TestModals(BaseClass):

    def test_Modals(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.closeCookiesWindows()
        time.sleep(1)
        hp.clickBtnModals()
        time.sleep(1)
        mp = ModalsPage(driver)
        mp.clickBtnSimpleModal()
        time.sleep(1)
        assert mp.showTxtFromSimpleModal() == "Hi, I’m a simple modal."
        time.sleep(1)
        mp.closeSimpleModal()
        time.sleep(1)
        mp.clickBtnFormModal()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(1)
        mp.completeFormModal("Pedro", "pedro18@gmail.com", "Este es el primer mensaje")
        time.sleep(2)









