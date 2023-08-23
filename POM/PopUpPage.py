import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class PopUpLocators:
    btnAlertPopUp = (By.ID, "alert")
    btnConfirmPopUp = (By.ID, "confirm")
    btnPromptPopUp = (By.ID, "prompt")
    tooltip = (By.CSS_SELECTOR, "#post-1055 > div > div.tooltip_1")
    confirmMessage = (By.ID, "confirmResult")
    promptResult = (By.ID, "promptResult")
    btnTooltip = (By.ID, "myTooltip")


class PopUpPage:

    def __init__(self, driver):
        self.driver = driver

    def clickBtnAlert(self):
        self.driver.find_element(*PopUpLocators.btnAlertPopUp).click()
        time.sleep(1)
        alert = Alert(self.driver)
        aux = alert.text
        time.sleep(1)
        alert.accept()
        return aux


    def clickBtnCancel(self):
        self.driver.find_element(*PopUpLocators.btnConfirmPopUp).click()
        time.sleep(1)
        alert = Alert(self.driver)
        time.sleep(1)
        alert.dismiss()


    def clickBtnConfirm(self):
        self.driver.find_element(*PopUpLocators.btnConfirmPopUp).click()
        time.sleep(1)
        alert = Alert(self.driver)
        time.sleep(1)
        alert.accept()

    def verifySatusMessage(self):
        return self.driver.find_element(*PopUpLocators.confirmMessage).text


    def clickConfirmPrompt(self, name):
        self.driver.find_element(*PopUpLocators.btnPromptPopUp).click()
        time.sleep(1)
        alert = Alert(self.driver)
        alert = self.driver.switch_to.alert
        time.sleep(1)
        alert.send_keys(name)
        alert.accept()
        time.sleep(2)


    def clickCancelPrompt(self):
        self.driver.find_element(*PopUpLocators.btnPromptPopUp).click()
        time.sleep(1)
        alert = Alert(self.driver)
        alert = self.driver.switch_to.alert
        time.sleep(1)
        alert.dismiss()
        time.sleep(2)


    def verifySatusPrompt(self):
        return self.driver.find_element(*PopUpLocators.promptResult).text

    def selectTooltip(self):
        self.driver.find_element(*PopUpLocators.tooltip).click()

    def verifyBtnToolTip(self):
        return self.driver.find_element(*PopUpLocators.btnTooltip).get_attribute('class')



