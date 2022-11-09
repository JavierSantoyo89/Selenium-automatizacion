## Importar todas las librerias necesarias
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class usandoUnitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driversSelenium\driverChrome\chromedriver.exe")
    
    def test_buscarPorXpath(self):
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        buscarPorXPath=driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        time.sleep(1)
        buscarPorXPath.send_keys('Selenium', Keys.RETURN)
        time.sleep(5)
    
    def tearDown(self):
        self.driver.close()
        ##Cierra la canexion

if __name__ == '__main__':
    unittest.main()
    ##Cierra la class

        ##Se recomienda para cuando cambien las rutas.

        ## Estructura de direcciones/objetos(XML)
        ##XPATH Relativo = Busca a partid del nodo (ej. /documentos)
        ##XPATH Absoluto = Busca desde la rais (ej. C;/Users/Documentos)