import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class AccordionsLocators:
    arrowAccordion = (By.CSS_SELECTOR, "#post-1261 > div summary")
    titleFromAccordion = (By.CSS_SELECTOR, "#post-1261 details > div > p")


class AccordionsPage:

    def __init__(self, driver):
        self.driver = driver

    def selectAccordion(self):
        return self.driver.find_element(*AccordionsLocators.arrowAccordion).click()

    def getTitleFromAccordion(self):
        return self.driver.find_element(*AccordionsLocators.titleFromAccordion).text









