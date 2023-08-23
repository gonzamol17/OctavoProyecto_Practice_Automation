import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class IframeLocators:
    iframeTitle = (By.CSS_SELECTOR, "#post-1129 > div > p:nth-child(1)")
    iframe1 = (By.ID, "frame2")
    iframe2 = (By.ID, "frame1")
    popularSearch = (By.CSS_SELECTOR, "#natgeo-search-results div > ul > li > a")
    glassIcon = (By.CSS_SELECTOR, "#fitt-analytics  ul > li:nth-child(2) > div")
    headerItemIfrem2 = (By.CSS_SELECTOR, "#main_navbar > ul >  li")



class IframePage:

    def __init__(self, driver):
        self.driver = driver


    def getTitle(self):
        return self.driver.find_element(*IframeLocators.iframeTitle).text

    def selectSearchIcon(self):
        self.driver.find_element(*IframeLocators.glassIcon).click()

    def getPopularSearchFristIframe(self):
        headers = self.driver.find_elements(*IframeLocators.popularSearch)
        for header in headers:
            print(header.text)
        print("\n")

    def getHeaderItemSecondIframe(self):
        headers = self.driver.find_elements(*IframeLocators.headerItemIfrem2)
        for header in headers:
            print(header.text)

    def getIframeOne(self):
        return self.driver.find_element(*IframeLocators.iframe1)

    def getIframeTwo(self):
        return self.driver.find_element(*IframeLocators.iframe2)








