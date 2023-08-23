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
from POM.SliderPage import SlidersPage


@pytest.mark.usefixtures("test_setup")
class TestSliders(BaseClass):

    def test_Sliders(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        hp.closeCookiesWindows()
        time.sleep(1)
        hp.clickBtnSliders()
        sp = SlidersPage(driver)
        print("Antes de mover el slider: " + sp.showCurrentValue())
        time.sleep(1)
        sp.moveSlider(50)
        time.sleep(1)
        print("Despues de mover el slider: " + sp.showCurrentValue())
        time.sleep(2)









