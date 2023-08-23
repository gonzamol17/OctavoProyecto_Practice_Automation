import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class SlidersLocators:
    currentValueMsg = (By.CSS_SELECTOR, "#post-2871 > div > div.coolslider > p:nth-child(3)")
    sliderItem = (By.ID, "slideMe")

class SlidersPage:

    def __init__(self, driver):
        self.driver = driver

    def showCurrentValue(self):
        return self.driver.find_element(*SlidersLocators.currentValueMsg).text

    def moveSlider(self, xvalue):
        action = ActionChains(self.driver)
        #action.click_and_hold(self.driver.find_element(*SlidersLocators.sliderItem)).move_by_offset(xvalue, 0).perform()
        action.drag_and_drop_by_offset((self.driver.find_element(*SlidersLocators.sliderItem)), xvalue, 0).perform()





