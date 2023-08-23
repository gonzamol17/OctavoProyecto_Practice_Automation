import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class JavaScriptDelayLocators:
    btnStart = (By.ID, "start")


class JavaScriptDelayPage:

    def __init__(self, driver):
        self.driver = driver

    def clickBtnStart(self):
        self.driver.find_element(*JavaScriptDelayLocators.btnStart).click()

    def checkBtnStartColor(self):
        return self.driver.find_element(*JavaScriptDelayLocators.btnStart).value_of_css_property('background-color')





