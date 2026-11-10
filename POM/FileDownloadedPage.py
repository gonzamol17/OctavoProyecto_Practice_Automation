import time
import os
from pathlib import Path

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class FileDownloadedLocators:
    downloadedWithOutPass = (By.CSS_SELECTOR, "a[rel='nofollow']")
    password = (By.CSS_SELECTOR, ".wp-block-paragraph> strong > strong")
    downloadedWithPass = (By.CSS_SELECTOR, "a.wpdm-download-link.wpdm-download-locked")
    txtPassword = (By.XPATH, "//input[@name='password']")
    btnSubmit = (By.CSS_SELECTOR, "body span.input-group-btn.input-group-append")
    optionCloseModal = (By.CSS_SELECTOR, "svg[stroke-linejoin='round']")
    iframe = (By.ID, "wpdm-lock-frame")

class FileDownloadedPage:

    def __init__(self, driver):
        self.driver = driver


    def downloadedFileWithoutPass(self):
        self.driver.find_element(*FileDownloadedLocators.downloadedWithOutPass).click()

    def verifyDownloadedFileNoPass(self):
        download_path = Path.home() / "Downloads" / "test.pdf"
        timeout = 30
        start_time = time.time()
        while time.time() - start_time < timeout:
            if download_path.exists():
                print("File download is completed")
                return
            time.sleep(1)
        raise Exception("File download is not completed")

    def downloadedFileWithPass(self):
        self.driver.find_element(*FileDownloadedLocators.downloadedWithPass).click()

    def verifyDownloadedFileYesPass(self, password):
        self.driver.find_element(*FileDownloadedLocators.txtPassword).send_keys(password)
        time.sleep(1)
        self.driver.find_element(*FileDownloadedLocators.btnSubmit).click()
        time.sleep(3)
        self.driver.find_element(*FileDownloadedLocators.optionCloseModal).click()
        downloads_path = Path.home() / "Downloads"
        while not os.path.exists(downloads_path):
            time.sleep(4)
        # check file
        time.sleep(1)
        file_path = downloads_path / "test.docx"
        if os.path.isfile(file_path):
            time.sleep(2)
            print("File download is completed")
        else:
            time.sleep(2)
            print("File download is not completed")

    def getPasswordFromPage(self):
        password = self.driver.find_element(*FileDownloadedLocators.password).text
        return password[1: -1]

    def getIframe(self):
        return self.driver.find_element(*FileDownloadedLocators.iframe)



