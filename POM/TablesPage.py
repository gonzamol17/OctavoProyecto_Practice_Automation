import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from collections import Counter


class TablesLocators:
    simpleTable = (By.CSS_SELECTOR, "#post-1076 > div > figure > table > tbody >tr")
    sliderItem = (By.ID, "slideMe")
    selector = (By.CSS_SELECTOR, "#tablepress-1_length > label > select")
    pagination = (By.CSS_SELECTOR, "#tablepress-1_info")
    countrySortableTable = (By.CSS_SELECTOR, "#tablepress-1 > tbody > tr > td.column-2")
    populationSortableTable = (By.CSS_SELECTOR, "#tablepress-1 > tbody > tr > td.column-3")
    rowTable = (By.CSS_SELECTOR, "#tablepress-1 > tbody > tr")
    columnTable = (By.CSS_SELECTOR, "#tablepress-1 > thead > tr > th")
    searchBar = (By.CSS_SELECTOR, "#tablepress-1_filter > label > input[type=search]")


class TablesPage:

    def __init__(self, driver):
        self.driver = driver

    def searchAValueIntoAFromTables(self, search):
        rows = self.driver.find_elements(*TablesLocators.simpleTable)
        aux = 1
        aux1 = 1
        n = 2
        for row in rows:
            if aux != 1:
                item = self.driver.find_element(By.CSS_SELECTOR, "#post-1076 > div > figure > table > tbody > tr:nth-child(" + str(n) + ") > td:nth-child(1)").text
                if item == search:
                    print("\nThe product was found, and its the following:")
                    print(self.driver.find_element(By.CSS_SELECTOR, "#post-1076 > div > figure > table > tbody > tr:nth-child(" + str(n) + ") > td:nth-child(1)").text)
                    return item
                    #break
                else:
                    if n == 4:
                        #aux1 = 2
                        break
                #print(n)
                n = n + 1
            else:
                aux = 2
        #if aux1 == 2:
        #    print("\nThe product you were looking for, was not found in the table")

    def getAllValuesFromTable(self):
        rows = self.driver.find_elements(*TablesLocators.simpleTable)
        aux = 1
        n = 2
        items = []
        for row in rows:
            if aux != 1:
                items.append(self.driver.find_element(By.CSS_SELECTOR, "#post-1076 > div > figure > table > tbody > tr:nth-child(" + str(n) + ") > td:nth-child(1)").text)
                n = n+1
            else:
                aux = 2
        return items

    # el siguiente método es para comparar dos listas que tienen el mismo numero de elementos y
    # el mismo orden de los elementos, solo sirve para ese caso, si están desordenados no va a funcionar
    def verifyEqualsList(self, items, listitems):
        for i in range(min(len(items), len(listitems))):
            if items[i] != listitems[i]:
                return False
        return len(items) == len(listitems)


    # el siguiente método es para comparar dos listas que tienen el mismo numero de elementos y
    # distinto orden, compara los elementos entre si no importa el orden en el que estén
    def verifyEqualsListWithoutOrder(self, items, listitems):
        return Counter(items) == Counter(listitems)


    def showNumberFromSelector(self):
        select = Select(self.driver.find_element(*TablesLocators.selector))
        return select.first_selected_option.text

    def showNumberFromPagination(self):
        return self.driver.find_element(*TablesLocators.pagination).text

    def searchTwoCountryRecordAndGetPopulation(self, country1, country2):
        countriesTable = self.driver.find_elements(*TablesLocators.countrySortableTable)
        #populationTable = self.driver.find_elements(*TablesLocators.populationSortableTable)
        #countries = []
        n = 1
        totPop = 0
        for country in countriesTable:
            n = n+1
            if country.text == country1 or country.text == country2:
                print(country.text)
                print(self.driver.find_element(By.CSS_SELECTOR, "#tablepress-1 > tbody > tr.row-" + str(n) + " > td.column-3").text)
                aux = self.driver.find_element(By.CSS_SELECTOR, "#tablepress-1 > tbody > tr.row-" + str(n) + " > td.column-3").text
                aux1 = float(aux.replace(',', ''))
                totPop = totPop+aux1

        return totPop



    def showAllElementsFromTables(self):
        rows = self.driver.find_elements(*TablesLocators.rowTable)
        columns = self.driver.find_elements(*TablesLocators.columnTable)
        countrows = len(rows)
        countcolumn = len(columns)
        print("\n"+"Rank"+"     " + "Country" + "      " + "Population(million)")
        for r in range(2, countrows+2):
            for c in range(1, countcolumn+1):
                value = self.driver.find_element(By.CSS_SELECTOR, "#tablepress-1 > tbody > tr.row-"+str(r)+"> td.column-"+str(c)+"").text
                print(value, end="        ")
            print()


    def searchACountryFromTables(self, country):
        countries = []
        self.driver.find_element(*TablesLocators.searchBar).send_keys(country)
        time.sleep(2)
        rows = self.driver.find_elements(*TablesLocators.rowTable)
        time.sleep(2)
        countrows = len(rows)
        #print(countrows)
        n = 1
        for r in range(1, countrows+1):
            aux = self.driver.find_element(By.CSS_SELECTOR, "#tablepress-1 > tbody>tr:nth-child(" + str(n) +")>td:nth-child(2)").text
            if country in aux:
                countries.append(aux)
            n = n+1
            print("Aca llegó")
        return countries
