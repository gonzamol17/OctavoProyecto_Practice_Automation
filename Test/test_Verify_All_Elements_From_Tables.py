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
from POM.TablesPage import TablesPage


@pytest.mark.usefixtures("test_setup")
class TestVerifyAllElementsFromTable(BaseClass):

    def test_Verify_All_Elements_From_Table(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(1)
        hp.closeCookiesWindows()
        time.sleep(1)
        hp.clickBtnTables()
        tp = TablesPage(driver)
        time.sleep(2)
        items = tp.getAllValuesFromTable()
        #print(items)
        listitems = ['Marbless', 'Oranges', 'Laptop']
        #el siguiente llamado es para comparar dos listas que tienen el mismo numero de elementos y
        #el mismo orden, solo sirve para ese caso, si están desordenados no va a funcionar
        #aux = tp.verifyEqualsList(items, listitems)

        # el siguiente llamado es para comparar dos listas que tienen el mismo numero de elementos y
        # distinto orden, compara los elementos entre si no importa el orden en el que estén
        aux = tp.verifyEqualsListWithoutOrder(items, listitems)
        assert aux is True
        time.sleep(2)









