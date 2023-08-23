import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class FormEventsLocators:
    fieldName = (By.ID, "g1103-name")
    allTheItemNames = (By.CSS_SELECTOR, "#contact-form-1103 div.grunion-field-checkbox-multiple-wrap.grunion-field-wrap > div span")
    allTheCheckboxes = (By.CSS_SELECTOR, "#contact-form-1103 div.grunion-field-checkbox-multiple-wrap.grunion-field-wrap > div > label> input")
    radioButtonNames = (By.CSS_SELECTOR, "#contact-form-1103 div.grunion-field-radio-wrap.grunion-field-wrap > div")
    radioButtonList = (By.CSS_SELECTOR, "#contact-form-1103 div.grunion-field-radio-wrap.grunion-field-wrap label input")
    dropdownSiblings = (By.CSS_SELECTOR, "#g1103-doyouhaveanysiblings-button")
    optionsDropdown = (By.CSS_SELECTOR, "#g1103-doyouhaveanysiblings-menu > li")
    emailField = (By.ID, "email")
    submitButton = (By.CSS_SELECTOR, "p.contact-submit:nth-child(2)>button.pushbutton-wide:nth-child(1)")
    formCompleted = (By.ID, "contact-form-1103")
    textBoxMessage = (By.ID, "contact-form-comment-message")


class FormEventsPage:

    def __init__(self, driver):
        self.driver = driver

    def insertName(self, name):
        self.driver.find_element(*FormEventsLocators.fieldName).send_keys(name)

    def selectOnlyOneItem(self, product):
        names = self.driver.find_elements(*FormEventsLocators.allTheItemNames)
        n = 1
        for name in names:
            if name.text == product:
                name.click()
                print(name.text)
                return self.driver.find_element(By.CSS_SELECTOR, "#contact-form-1103 div.grunion-field-checkbox-multiple-wrap.grunion-field-wrap label:nth-child(" + str(n) + ") > input").is_selected()
            n = n+1


    def selectAllItems(self):
        checkboxes = self.driver.find_elements(*FormEventsLocators.allTheCheckboxes)
        n = 1
        list = []
        for checkbox in checkboxes:
            checkbox.click()
            #print("Item"+str(n)+", está seleccionado:")
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
        options = self.driver.find_elements(*FormEventsLocators.optionsDropdown)
        for option in options:
            if option.text == opt:
                #print(option.text)
                option.click()

    def verifyValueInDropdown(self):
        return self.driver.find_element(*FormEventsLocators.dropdownSiblings).text

    def fillEmailField(self, email):
        self.driver.find_element(*FormEventsLocators.emailField).send_keys(email)

    def sendForm(self):
        self.driver.find_element(*FormEventsLocators.submitButton).click()

    def returnForm(self):
        return self.driver.find_element(*FormEventsLocators.formCompleted).text

    def completeBoxMessage(self, message):
        self.driver.find_element(*FormEventsLocators.textBoxMessage).send_keys(message)
