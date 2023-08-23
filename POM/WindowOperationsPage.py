import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class WindowOperationsLocators:
    btnNewTab = (By.CSS_SELECTOR, "#post-1147 > div > p:nth-child(2) > button")
    btnReplaceWindow = (By.CSS_SELECTOR, "#post-1147 > div > p:nth-child(4) > button")
    btnNewWindow = (By.CSS_SELECTOR, "#post-1147 > div > p:nth-child(6) > button")



class WindowOperationsPage:

    def __init__(self, driver):
        self.driver = driver

    def selectNewTabButton(self):
        parent_handle = self.driver.current_window_handle
        self.driver.find_element(*WindowOperationsLocators.btnNewTab).click()
        time.sleep(1)
        all_handles = self.driver.window_handles
        print(self.driver.current_url)
        for handle in all_handles:
            time.sleep(1)
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                if self.driver.current_url == "https://automatenow.io/":
                    print(self.driver.current_url)
                    self.driver.close()
                    time.sleep(1)
        self.driver.switch_to.window(parent_handle)
        print(self.driver.current_url)
        return self.driver.current_url


    def selectReplaceWindowButton(self):
        handle1 = self.driver.current_window_handle
        print(self.driver.current_url)
        self.driver.find_element(*WindowOperationsLocators.btnReplaceWindow).click()
        time.sleep(1)
        handle2 = self.driver.current_window_handle
        print(self.driver.current_url)
        return self.driver.current_url


    def selectNewWindowButton(self):
        original_handle = self.driver.current_window_handle
        print(original_handle)
        print(self.driver.current_url)
        self.driver.find_element(*WindowOperationsLocators.btnNewWindow).click()
        time.sleep(1)
        all_handles = self.driver.window_handles
        for handle in all_handles:
            time.sleep(1)
            print(handle)
            #print(self.driver.current_url)
            if handle != original_handle:
                self.driver.switch_to.window(handle)
                if self.driver.current_url == "https://automatenow.io/":
                    print(self.driver.current_url)
                    self.driver.close()
        self.driver.switch_to.window(original_handle)
        print(self.driver.current_url)
        return self.driver.current_url




