import time
import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class FileUploadLocators:
    btnUploadIt = (By.CSS_SELECTOR, "#wpcf7-f6157-p1037-o1 p:nth-child(2) > input")
    txtMessage = (By.CSS_SELECTOR, "#wpcf7-f6157-p1037-o1 > form > div.wpcf7-response-output")


class FileUploadPage:

    def __init__(self, driver):
        self.driver = driver

    def selectUploadItBtn(self):
        self.driver.find_element(*FileUploadLocators.btnUploadIt).click()
        #element = WebDriverWait(self.driver, 20).until(
        #    ec.presence_of_element_located((By.CSS_SELECTOR, "#wpcf7-f6157-p1037-o1 > form > div.wpcf7-response-output")))
        time.sleep(2)
        return self.driver.find_element(*FileUploadLocators.txtMessage).text









