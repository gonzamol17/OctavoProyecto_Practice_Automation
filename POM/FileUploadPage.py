import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FileUploadLocators:
    btnUploadIt = (By.XPATH, "//input[@id='upload-btn']")
    txtMessage = (By.XPATH, "//span[contains(text(),'Please fill out this field.')]")
    btnUploadFile = (By.CSS_SELECTOR, "span>#file-upload")
    txtSuccessMsg = (By.CSS_SELECTOR, "div.wpcf7-response-output")


class FileUploadPage:

    def __init__(self, driver):
        self.driver = driver

    def selectUploadItBtn(self):
        self.driver.find_element(*FileUploadLocators.btnUploadIt).click()
        #element = WebDriverWait(self.driver, 20).until(
        #    ec.presence_of_element_located((By.CSS_SELECTOR, "#wpcf7-f6157-p1037-o1 > form > div.wpcf7-response-output")))
        time.sleep(2)
        return self.driver.find_element(*FileUploadLocators.txtMessage).text

    def selectUploadAFilebtn(self):
        self.driver.find_element(*FileUploadLocators.btnUploadIt).click()

    # Subir archivo
    def uploadFileSuccess(self, filePath):
        self.driver.find_element(*FileUploadLocators.btnUploadFile).send_keys(filePath)

    # Obtener mensaje de validación HTML5
    def getValidationMessage(self):
        element = self.driver.find_element(*FileUploadLocators.btnUploadFile)
        validation_message = self.driver.execute_script(
            "return arguments[0].validationMessage;",
            element
        )
        return validation_message

    def showSuccessMsg(self):
        wait = WebDriverWait(self.driver, 10)
        success_message = wait.until(
            EC.visibility_of_element_located(
                FileUploadLocators.txtSuccessMsg
            )
        )

        return success_message.text





