import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ClickEventsLocators:
    valueMsg = (By.CSS_SELECTOR, "#demo")
    btnCat = (By.XPATH, "// b[contains(text(), 'Cat')]")
    btnDog = (By.XPATH, "// b[contains(text(), 'Dog')]")
    btnPig = (By.XPATH, "// b[contains(text(), 'Pig')]")
    btnCow = (By.XPATH, "// b[contains(text(), 'Cow')]")


class ClickEventsPage:

    def __init__(self, driver):
        self.driver = driver

    def selectBtnCat(self):
        self.driver.find_element(*ClickEventsLocators.btnCat).click()
        if self.driver.find_element(*ClickEventsLocators.btnCat).text == "Cat":
            return self.driver.find_element(*ClickEventsLocators.valueMsg).text
        else:
            print("this is not a Cat button")

    def selectBtnDog(self):
        self.driver.find_element(*ClickEventsLocators.btnDog).click()
        if self.driver.find_element(*ClickEventsLocators.btnDog).text == "Dog":
            return self.driver.find_element(*ClickEventsLocators.valueMsg).text
        else:
            print("this is not a Dog button")

    def selectBtnPig(self):
        self.driver.find_element(*ClickEventsLocators.btnPig).click()
        if self.driver.find_element(*ClickEventsLocators.btnPig).text == "Pig":
            return self.driver.find_element(*ClickEventsLocators.valueMsg).text
        else:
            print("this is not a Pig button")

    def selectBtnCow(self):
        self.driver.find_element(*ClickEventsLocators.btnCow).click()
        if self.driver.find_element(*ClickEventsLocators.btnCow).text == "Cow":
            return self.driver.find_element(*ClickEventsLocators.valueMsg).text
        else:
            print("this is not a Cow button")
