import re
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
from POM.FileUploadPage import FileUploadPage


@pytest.mark.usefixtures("test_setup")
class TestFileUpload(BaseClass):

    def test_FileUpload(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        hp.closeCookiesWindows()
        time.sleep(1)
        hp.clickBtnFileUpload()
        time.sleep(1)
        fu = FileUploadPage(driver)
        text = fu.selectUploadItBtn()
        assert text == "File upload complete!"
        time.sleep(2)










