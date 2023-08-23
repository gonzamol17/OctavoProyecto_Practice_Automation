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
class TestFormEventsCompleteAndSendForm(BaseClass):

    def test_FormEvents_CompleteAndSendForm(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        hp.closeCookiesWindows()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(1)
        hp.clickBtnFormEvents()
        time.sleep(1)
        time.sleep(1)
        fe = FormEventsPage(driver)
        # para ingresar el nombre
        name = "Pedro"
        fe.insertName(name)
        time.sleep(1)
        product = "Wine"
        isSelected = fe.selectOnlyOneItem(product)
        assert isSelected is True
        #para elegir el color
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(1)
        color = "Green"
        isSelected = fe.showRadioButtonSection(color)
        assert isSelected is True
        # para elegir el color
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(1)
        option = "Yes"
        fe.chooseOneOptionFromDropdown(option)
        assert fe.verifyValueInDropdown() == option
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(2)
        email = "pepe@hotmail.com"
        fe.fillEmailField(email)
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(1)
        message = "This is first content, that i fill in this box"
        fe.completeBoxMessage(message)
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 900)")
        time.sleep(2)
        fe.sendForm()
        time.sleep(1)
        print(fe.returnForm())
        time.sleep(2)










