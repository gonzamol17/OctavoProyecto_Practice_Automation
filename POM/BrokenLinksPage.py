import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BrokenLinksLocators:
    hyperlinkBrokenLink = (By.XPATH, "//a[contains(text(),'broken link')]")


class BrokenLinksPage:

    def __init__(self, driver):
        self.driver = driver

    def selectHyperlink(self):
        self.driver.find_element(*BrokenLinksLocators.hyperlinkBrokenLink).click()
        time.sleep(2)
        return self.driver.current_url






