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
from POM.FormEventsPage import FormEventsPage


@pytest.mark.usefixtures("test_setup")
class TestFormEventsSelectARadioButton(BaseClass):

    def test_FormEvents_Select_A_RadioButton(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        hp.closeCookiesWindows()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 150)")
        time.sleep(1)
        hp.clickBtnFormEvents()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 150)")
        fe = FormEventsPage(driver)
        time.sleep(1)
        color = "Green"
        isSelected = fe.showRadioButtonSection(color)
        assert isSelected is True
        print("Y el color elegido, está seleccionado")
        time.sleep(2)










