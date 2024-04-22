import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class FormEventsLocators:
    fieldName = (By.ID, "name")
    allTheItemNames = (By.XPATH, "//input[@name='fav_drink']")
    allTheCheckboxes = (By.XPATH, "//input[contains(@type, 'checkbox')]")
    radioButtonNames = (By.CSS_SELECTOR, "#contact-form-1103 div.grunion-field-radio-wrap.grunion-field-wrap > div")
    radioButtonList = (By.XPATH, "//input[@name='fav_color']")
    dropdownSiblings = (By.ID, "siblings")
    listOptionsDropdown = (By.XPATH, "//option[contains(@data-cy, 'siblings')]")
    emailField = (By.ID, "email")
    submitButton = (By.ID, "submit-btn")
    formCompleted = (By.ID, "contact-form-1103")
    textBoxMessage = (By.ID, "message")


class FormEventsPage:

    def __init__(self, driver):
        self.driver = driver

    def insertName(self, name):
        self.driver.find_element(*FormEventsLocators.fieldName).send_keys(name)

    def selectOnlyOneItem(self, product):
        names = self.driver.find_elements(*FormEventsLocators.allTheItemNames)
        for name in names:
            if name.get_attribute("value") == product:
                name.click()
                print(name.get_attribute("value"))
                #return self.driver.find_element(By.XPATH, "//label[contains(text(),'"+name.get_attribute("value")+"')]").is_selected()
                return self.driver.find_element(By.XPATH, "//input[@value='"+name.get_attribute("value")+"']").is_selected()



    def selectAllItems(self):
        checkboxes = self.driver.find_elements(*FormEventsLocators.allTheCheckboxes)
        n = 1
        list = []
        for checkbox in checkboxes:
            checkbox.click()
            time.sleep(1)
            #print(self.driver.find_element(By.XPATH, "//label[contains(@for,'drink"+str(n)+"')]").is_enabled())
            print("Item"+str(n)+", está seleccionado")
            list.append(checkbox.is_selected())
            time.sleep(1)
            n = n+1
        return list


    def showRadioButtonSection(self, color):
        radios = self.driver.find_elements(*FormEventsLocators.radioButtonList)
        for radio in radios:
            if radio.get_attribute('value') == color:
                radio.click()
                print("El color seleccionado es: "+radio.get_attribute('value'))
                return radio.is_selected()

    def chooseOneOptionFromDropdown(self, opt):
        self.driver.find_element(*FormEventsLocators.dropdownSiblings).click()
        options = self.driver.find_elements(*FormEventsLocators.listOptionsDropdown)
        for option in options:
            if option.text == opt:
                print(option.text)
                option.click()

    def verifyValueInDropdown(self, option):
        #return self.driver.find_element(*FormEventsLocators.optionsDropdown).text
        return self.driver.find_element(By.XPATH, "//option[contains(text(),'"+option+"')]").text

    def fillEmailField(self, email):
        self.driver.find_element(*FormEventsLocators.emailField).send_keys(email)

    def sendForm(self):
        self.driver.find_element(*FormEventsLocators.submitButton).click()

    def returnForm(self):
        alert = self.driver.switch_to.alert
        message = alert.text
        alert.accept()
        return message
        #return self.driver.find_element(*FormEventsLocators.formCompleted).text

    def completeBoxMessage(self, message):
        self.driver.find_element(*FormEventsLocators.textBoxMessage).send_keys(message)
