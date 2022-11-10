import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec ## Es una libreria para usar condiciones


class unit_test(unittest.TestCase):
    ## Carga el webdriver en una variable para ser usada
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driversSelenium\driverChrome\chromedriver.exe")
    
    def testExplicitWait(self):
        driver = self.driver
        driver.get("http://www.google.com")
        try: ##Crear ciclo Try/finaly
            ## Buscame el elemento hast 10 veces del elemento q
            ## WebDriverWait = Busca elemento hasta que
            ## presence_of_element_located = Busca un elemento por Id/Name
            element = WebDriverWait(driver, 10).until(Ec.presence_of_element_located((By.NAME, 'q')))
        finally:
            ## Cierra el uso del driver para que no se ciclo
            driver.quit()


if __name__ == '__main__':
    unittest.main()