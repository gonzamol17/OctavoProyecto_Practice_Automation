import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CalendarsLocators:
    txtFieldCalendar = (By.ID, "g1065-1-selectorenteradate")
    backArrow = (By.CSS_SELECTOR, "#ui-datepicker-div a.ui-datepicker-prev.ui-corner-all")
    nextArrow = (By.CSS_SELECTOR, "button.dp-focusable.dp-prev")
    month = (By.CSS_SELECTOR, "button.dp-focusable.dp-cal-month")
    year = (By.CSS_SELECTOR, "button.dp-focusable.dp-cal-year")
    dayWeek = (By.CSS_SELECTOR, "#ui-datepicker-div thead>tr>th")
    day = (By.CSS_SELECTOR, "#ui-datepicker-div tbody")


class CalendarsPage:

    def __init__(self, driver):
        self.driver = driver

    def openCalendar(self):
        self.driver.find_element(*CalendarsLocators.txtFieldCalendar).click()

    def verifyMonthAndYear(self, month, year):
        # while self.driver.find_element(*CalendarsLocators.year).text == year:
        #     if self.driver.find_element(*CalendarsLocators.month).text == month:
        #         break
        #     else:
        #         time.sleep(1)
        #         self.driver.find_element(*CalendarsLocators.nextArrow).click()
        #
        # while self.driver.find_element(*CalendarsLocators.year).text != year:
        #     time.sleep(1)
        #     self.driver.find_element(*CalendarsLocators.nextArrow).click()
        #
        # while self.driver.find_element(*CalendarsLocators.month).text != month:
        #     time.sleep(1)
        #     self.driver.find_element(*CalendarsLocators.nextArrow).click()
        while True:

            current_month = self.driver.find_element(
                *CalendarsLocators.month
            ).text.strip()

            current_year = self.driver.find_element(
                *CalendarsLocators.year
            ).text.strip()

            print(current_month, current_year)

            if current_month == month and current_year == year:
                break

            self.driver.find_element(
                *CalendarsLocators.nextArrow
            ).click()

            time.sleep(0.5)

        #print(self.driver.find_element(*CalendarsLocators.month).text)
        #print(self.driver.find_element(*CalendarsLocators.year).text)


    def verifyWeekDay(self, day):
        # weeks = self.driver.find_elements(By.CSS_SELECTOR, "#ui-datepicker-div > table > tbody > tr > td")
        # for week in weeks:
        #     if week.get_attribute('class') != " ui-datepicker-other-month ui-datepicker-unselectable ui-state-disabled":
        #         if week.text == day:
        #             week.click()
        days = self.driver.find_elements(By.CSS_SELECTOR, "button.dp-day")
        for d in days:
            classes = d.get_attribute("class")
            # Ignorar días deshabilitados
            if "dp-edge-day" in classes:
                continue

            if d.text == day:
                d.click()
                break


    def showDateSelected(self):
        return self.driver.find_element(*CalendarsLocators.txtFieldCalendar).get_attribute('value')



