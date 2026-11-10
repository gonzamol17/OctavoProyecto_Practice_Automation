import re
import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.FileUploadPage import FileUploadPage


class TestFileUpload(BaseClass):

    def test_UploadFileWithAFile(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        #hp.closeCookiesWindows()
        driver.execute_script("window.scrollTo(0, 1500)")
        time.sleep(1)
        hp.clickBtnFileUpload()
        time.sleep(1)
        fu = FileUploadPage(driver)
        download_path = os.path.join(os.path.expanduser("~"), "Downloads")
        file_path = os.path.join(download_path, "test.docx")
        assert os.path.exists(file_path)
        fu.uploadFileSuccess(file_path)
        fu.selectUploadAFilebtn()
        #time.sleep(3)
        text = fu.showSuccessMsg()
        assert text == "Thank you for your message. It has been sent."
        time.sleep(2)










