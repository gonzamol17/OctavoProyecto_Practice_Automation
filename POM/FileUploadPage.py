import time

from selenium.webdriver.common.by import By

class FileUploadLocators:
    btnUploadIt = (By.XPATH, "//input[@id='upload-btn']")
    txtMessage = (By.XPATH, "//span[contains(text(),'Please fill out this field.')]")


class FileUploadPage:

    def __init__(self, driver):
        self.driver = driver

    def selectUploadItBtn(self):
        self.driver.find_element(*FileUploadLocators.btnUploadIt).click()
        #element = WebDriverWait(self.driver, 20).until(
        #    ec.presence_of_element_located((By.CSS_SELECTOR, "#wpcf7-f6157-p1037-o1 > form > div.wpcf7-response-output")))
        time.sleep(2)
        return self.driver.find_element(*FileUploadLocators.txtMessage).text









