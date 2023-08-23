import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CarouselsLocators:
    prevArrow = (By.ID, "12345-prev")
    nextArrow = (By.ID, "12345-next")
    itemsCarousel = (By.ID, "main")


class CarouselsPage:

    def __init__(self, driver):
        self.driver = driver


    def moveNextItem(self):
        aux = 3
        while aux <= 7:
            time.sleep(1)
            self.driver.find_element(*CarouselsLocators.nextArrow).click()
            aux = aux + 1

    def movePrevItem(self):
        aux = 3
        while aux <= 7:
            time.sleep(1)
            self.driver.find_element(*CarouselsLocators.prevArrow).click()
            aux = aux + 1










