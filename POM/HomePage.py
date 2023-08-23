import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class HomePageLocators:
    btnJavaScriptDelay = (By.XPATH, "//a[contains(text(),'JavaScript Delays')]")
    btnSliders = (By.XPATH, "//a[contains(text(),'Sliders')]")
    btnTables = (By.XPATH, "//a[contains(text(),'Tables')]")
    cookiesWindow = (By.ID, "cookie_action_close_header")
    btnAds = (By.XPATH, "//a[contains(text(),'Ads')]")
    btnClickEvents = (By.XPATH, "//a[contains(text(),'Click Events')]")
    btnFormEvents = (By.XPATH, "//a[contains(text(),'Form Fields')]")
    btnCalendars = (By.XPATH, "//a[contains(text(),'Calendars')]")
    btnWindowOperations = (By.XPATH, "//a[contains(text(),'Window Operations')]")
    btnGestures = (By.XPATH, "//a[contains(text(),'Gestures')]")
    btnSpinner = (By.XPATH, "//a[contains(text(),'Spinners')]")
    btnPopUps = (By.XPATH, "//a[contains(text(),'Popups')]")
    btnModals = (By.XPATH, "//a[contains(text(),'Modals')]")
    btnHover = (By.XPATH, "//a[contains(text(),'Hover')]")
    btnIFrames = (By.XPATH, "//a[contains(text(),'Iframes')]")
    btnCarousels = (By.XPATH, "//a[contains(text(),'Carousels')]")
    btnFileDownloaded = (By.XPATH, "//a[contains(text(),'File Download')]")
    btnFileUpload = (By.XPATH, "//a[contains(text(),'File Upload')]")
    btnBrokenLinks = (By.XPATH, "//a[contains(text(),'Broken Links')]")
    btnBrokenImages = (By.XPATH, "//a[contains(text(),'Broken Images')]")
    btnAccordions = (By.XPATH, "//a[contains(text(),'Accordions')]")


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def clickBtnJavaScriptDelay(self):
        self.driver.find_element(*HomePageLocators.btnJavaScriptDelay).click()

    def clickBtnSliders(self):
        self.driver.find_element(*HomePageLocators.btnSliders).click()

    def clickBtnTables(self):
        self.driver.find_element(*HomePageLocators.btnTables).click()

    def clickBtnAds(self):
        self.driver.find_element(*HomePageLocators.btnAds).click()

    def clickBtnClickEvents(self):
        self.driver.find_element(*HomePageLocators.btnClickEvents).click()

    def clickBtnFormEvents(self):
        self.driver.find_element(*HomePageLocators.btnFormEvents).click()

    def clickBtnCalendars(self):
        self.driver.find_element(*HomePageLocators.btnCalendars).click()

    def clickBtnWindowOperations(self):
        self.driver.find_element(*HomePageLocators.btnWindowOperations).click()

    def clickBtnGestures(self):
        self.driver.find_element(*HomePageLocators.btnGestures).click()

    def clickBtnSpinner(self):
        self.driver.find_element(*HomePageLocators.btnSpinner).click()

    def clickBtnPopUps(self):
        self.driver.find_element(*HomePageLocators.btnPopUps).click()

    def clickBtnModals(self):
        self.driver.find_element(*HomePageLocators.btnModals).click()

    def clickBtnHover(self):
        self.driver.find_element(*HomePageLocators.btnHover).click()

    def clickBtnIFrames(self):
        self.driver.find_element(*HomePageLocators.btnIFrames).click()

    def clickBtnCarousels(self):
        self.driver.find_element(*HomePageLocators.btnCarousels).click()

    def clickBtnFileDownloaded(self):
        self.driver.find_element(*HomePageLocators.btnFileDownloaded).click()

    def clickBtnFileUpload(self):
        self.driver.find_element(*HomePageLocators.btnFileUpload).click()

    def clickBtnBrokenLinks(self):
        self.driver.find_element(*HomePageLocators.btnBrokenLinks).click()

    def clickBtnBrokenImages(self):
        self.driver.find_element(*HomePageLocators.btnBrokenImages).click()

    def clickBtnAccordions(self):
        self.driver.find_element(*HomePageLocators.btnAccordions).click()

    def closeCookiesWindows(self):
        self.driver.find_element(*HomePageLocators.cookiesWindow).click()




