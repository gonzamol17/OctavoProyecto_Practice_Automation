import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BrokenImagesLocators:
    allImages = (By.CSS_SELECTOR, "#post-1218 > div > div.wp-block-group.is-layout-flow.wp-block-group-is-layout-flow > div img")


class BrokenImagesPage:

    def __init__(self, driver):
        self.driver = driver

    def getAllImages(self):
        images = self.driver.find_elements(*BrokenImagesLocators.allImages)
        tot = len(images)
        print("The total of images are: "+str(tot))
        n = 1
        b = 0
        for image in images:
            if "Broken Image" in image.get_attribute('alt'):
                print("The image "+str(n)+" was broken")
                n = n+1
                b = 1
            else:
                print("The image "+str(n)+" is visualized successfully")
                n = n + 1
        return b







