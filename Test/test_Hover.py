import time
import pytest
import unittest
import HtmlTestRunner
from Utils import Utils as Utils
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.HoverPage import HoverPage
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))


@pytest.mark.usefixtures("test_setup")
class TestHover(BaseClass):

    def test_Hover(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.closeCookiesWindows()
        time.sleep(1)
        hp.clickBtnHover()
        time.sleep(1)
        hrp = HoverPage(driver)
        assert hrp.getTitleBeforeHover() == "Mouse over me"
        time.sleep(2)
        hrp.doHoverOverTitle()
        time.sleep(1)
        assert hrp.getTitleAfterHover() == "You did it!"
        time.sleep(1)
        assert hrp.getColorTitleAfterHover() == "rgba(0, 128, 0, 1)"
        time.sleep(2)









