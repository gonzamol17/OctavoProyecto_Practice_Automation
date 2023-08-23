import time
import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class FileDownloadedLocators:
    downloadedWithOutPass = (By.CSS_SELECTOR, "#post-1042 > div > div:nth-child(2) > div > div > div > div.ml-3 > a")
    password = (By.CSS_SELECTOR, "#post-1042 > div > p:nth-child(4) > strong > strong")
    downloadedWithPass = (By.CSS_SELECTOR, "#post-1042 > div > div:nth-child(5) > div > div > div > div.ml-3 > a")
    txtPassword = (By.XPATH, "//input[@name='password']")
    btnSubmit = (By.CSS_SELECTOR, "body span.input-group-btn.input-group-append")
    optionCloseModal = (By.CSS_SELECTOR, "#wpdm-locks > div > div > div.text-center.mt-3.mb-3 > button")
    iframe = (By.ID, "wpdm-lock-frame")

class FileDownloadedPage:

    def __init__(self, driver):
        self.driver = driver


    def downloadedFileWithoutPass(self):
        self.driver.find_element(*FileDownloadedLocators.downloadedWithOutPass).click()

    def verifyDownloadedFileNoPass(self):
        while not os.path.exists('C:\\Users\\admin\\Downloads'):
            time.sleep(3)
        # check file
        if os.path.isfile('C:\\Users\\admin\\Downloads\\test.pdf'):
            time.sleep(2)
            print("File download is completed")
        else:
            time.sleep(2)
            print("File download is not completed")

    def downloadedFileWithPass(self):
        self.driver.find_element(*FileDownloadedLocators.downloadedWithPass).click()

    def verifyDownloadedFileYesPass(self, password):
        self.driver.find_element(*FileDownloadedLocators.txtPassword).send_keys(password)
        time.sleep(1)
        self.driver.find_element(*FileDownloadedLocators.btnSubmit).click()
        time.sleep(3)
        self.driver.find_element(*FileDownloadedLocators.optionCloseModal).click()
        while not os.path.exists('C:\\Users\\admin\\Downloads'):
            time.sleep(4)
        # check file
        time.sleep(1)
        if os.path.isfile('C:\\Users\\admin\\Downloads\\test.docx'):
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



