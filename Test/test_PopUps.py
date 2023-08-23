import time
import pytest
import unittest
import HtmlTestRunner
from Utils import Utils as Utils
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.PopUpPage import PopUpPage
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))


@pytest.mark.usefixtures("test_setup")
class TestPopUps(BaseClass):

    def test_PopUps(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.closeCookiesWindows()
        time.sleep(1)
        hp.clickBtnPopUps()
        time.sleep(1)
        pu = PopUpPage(driver)
        messageAlert = pu.clickBtnAlert()
        assert messageAlert == "Hi there, pal!"
        time.sleep(1)
        pu.clickBtnCancel()
        assert pu.verifySatusMessage() == "Cancel it is!"
        time.sleep(1)
        pu.clickBtnConfirm()
        assert pu.verifySatusMessage() == "OK it is!"
        time.sleep(1)
        name = "Pedro"
        pu.clickConfirmPrompt(name)
        assert pu.verifySatusPrompt() == "Nice to meet you, "+name+"!"
        time.sleep(1)
        pu.clickCancelPrompt()
        assert pu.verifySatusPrompt() == "Fine, be that way..."
        time.sleep(1)
        pu.selectTooltip()
        assert "show" in pu.verifyBtnToolTip()
        time.sleep(1)
        pu.selectTooltip()
        time.sleep(1)
        assert "tooltip_text" == pu.verifyBtnToolTip()
        time.sleep(2)









