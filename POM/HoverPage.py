import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class HoverLocators:
    leyendWithOutHover = (By.ID, "mouse_over")



class HoverPage:

    def __init__(self, driver):
        self.driver = driver

    def doHoverOverTitle(self):
        a = ActionChains(self.driver)
        #m = driver.find_element_by_link_text("Enabled")
        a.move_to_element(self.driver.find_element(*HoverLocators.leyendWithOutHover)).perform()

    def getTitleBeforeHover(self):
        return self.driver.find_element(*HoverLocators.leyendWithOutHover).text

    def getTitleAfterHover(self):
        return self.driver.find_element(*HoverLocators.leyendWithOutHover).text

    def getColorTitleAfterHover(self):
        return self.driver.find_element(*HoverLocators.leyendWithOutHover).value_of_css_property('color')








