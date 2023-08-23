import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class ModalsLocators:
    simpleModal = (By.ID, "simpleModal")
    formModal = (By.ID, "formModal")
    messageSimpleModal = (By.CSS_SELECTOR, "#popmake-1318 > div.pum-content.popmake-content")
    closeSimpleModal = (By.CSS_SELECTOR, "#popmake-1318 > button")
    fieldNameModal = (By.ID, "g1051-name")
    fieldEmailModal = (By.ID, "g1051-email")
    fieldMessageModal = (By.ID, "contact-form-comment-g1051-message")
    btnAcceptModal = (By.CSS_SELECTOR, "#contact-form-1051 button")


class ModalsPage:

    def __init__(self, driver):
        self.driver = driver

    def clickBtnSimpleModal(self):
        self.driver.find_element(*ModalsLocators.simpleModal).click()

    def showTxtFromSimpleModal(self):
        return self.driver.find_element(*ModalsLocators.messageSimpleModal).text

    def closeSimpleModal(self):
        self.driver.find_element(*ModalsLocators.closeSimpleModal).click()

    def clickBtnFormModal(self):
        self.driver.find_element(*ModalsLocators.formModal).click()

    def completeFormModal(self, name, email, message):
        self.driver.find_element(*ModalsLocators.fieldNameModal).send_keys(name)
        time.sleep(1)
        self.driver.find_element(*ModalsLocators.fieldEmailModal).send_keys(email)
        time.sleep(1)
        self.driver.find_element(*ModalsLocators.fieldMessageModal).send_keys(message)
        time.sleep(1)
        self.driver.find_element(*ModalsLocators.btnAcceptModal).click()
        time.sleep(1)






