import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class AdsLocators:
    valueMsg = (By.CSS_SELECTOR, "#post-1274 > div > p")
    popup = (By.CSS_SELECTOR, "#popmake-1272 > button")
    textFromPopUp = (By.CSS_SELECTOR, "#post-1274 > div > p")


class AdsPage:

    def __init__(self, driver):
        self.driver = driver

    def showCurrentValue(self):
        return self.driver.find_element(*AdsLocators.valueMsg).text

    def verifyPopUpIsPresented(self):
        element = WebDriverWait(self.driver, 20).until(ec.presence_of_element_located((By.CSS_SELECTOR, "#popmake-1272 > button")))
        element.click()
        return self.driver.find_element(*AdsLocators.textFromPopUp).text






