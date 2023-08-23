import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class GesturesLocators:
    boxToMove = (By.ID, "moveMeHeader")

class GesturesPage:

    def __init__(self, driver):
        self.driver = driver

    def moveTheBox(self):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(self.driver.find_element(*GesturesLocators.boxToMove), 553, 41).perform()

