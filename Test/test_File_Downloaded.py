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
from POM.FileDownloadedPage import FileDownloadedPage


@pytest.mark.usefixtures("test_setup")
class TestFileDownloaded(BaseClass):

    def test_FileDownloaded(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        hp.closeCookiesWindows()
        time.sleep(1)
        hp.clickBtnFileDownloaded()
        time.sleep(1)
        fd = FileDownloadedPage(driver)
        fd.downloadedFileWithoutPass()
        time.sleep(1)
        fd.verifyDownloadedFileNoPass()
        time.sleep(1)
        password = fd.getPasswordFromPage()
        time.sleep(1)
        fd.downloadedFileWithPass()
        time.sleep(1)
        driver.switch_to.frame(fd.getIframe())
        time.sleep(1)
        fd.verifyDownloadedFileYesPass(password)
        time.sleep(2)










