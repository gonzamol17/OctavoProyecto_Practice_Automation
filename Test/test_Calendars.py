import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import HtmlTestRunner
from Utils import Utils as Utils
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.CalendarPage import CalendarsPage


@pytest.mark.usefixtures("test_setup")
class TestCalendars(BaseClass):

    def test_Calendar(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        hp.closeCookiesWindows()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(1)
        hp.clickBtnCalendars()
        cl = CalendarsPage(driver)
        time.sleep(1)
        cl.openCalendar()
        time.sleep(1)
        month = "September"
        year = "2024"
        cl.verifyMonthAndYear(month, year)
        time.sleep(1)
        day = "4"
        cl.verifyWeekDay(day)
        time.sleep(1)
        date = cl.showDateSelected()
        dateExpected = month+" "+day+", "+year
        #assert date == month+" "+day+", "+year
        assert date == dateExpected
        print(dateExpected)
        time.sleep(2)










