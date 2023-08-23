import time
import pytest
import unittest
import HtmlTestRunner
from Utils import Utils as Utils
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.SpinnerPage import SpinnerPage
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))


@pytest.mark.usefixtures("test_setup")
class TestSpinner(BaseClass):

    def test_Spinner(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        hp.closeCookiesWindows()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(1)
        hp.clickBtnSpinner()
        sp = SpinnerPage(driver)
        assert sp.showIsSpinner() is True
        print("El spinner se ha podido visualizar")
        time.sleep(1)










