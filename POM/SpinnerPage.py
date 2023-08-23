import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SpinnerLocators:
    spinner = (By.CSS_SELECTOR, "#post-7078>div>div.spinner")


class SpinnerPage:

    def __init__(self, driver):
        self.driver = driver

    def showIsSpinner(self):
        element = WebDriverWait(self.driver, 4).until(ec.presence_of_element_located((By.CSS_SELECTOR, "#post-7078>div>div.spinner")))
        return element.is_displayed()
