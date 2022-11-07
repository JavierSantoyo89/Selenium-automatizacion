import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class usandoUnitTest(unittest.TestCase):
    ## Inivcializa driver(SetUp) (Self = return)
    def setUp(self):
        self.drver= webdriver.Chrome(executable_path=r"C:\driversSelenium\driverChrome\chromedriver.exe")
    
    ## Siempre poner 'test_' para que el sistema sepa que ejecutar ##
    def test_buscar(self):
        driver = self.drver
        driver.get("http://www.google.com")
        ##Asserting = se asegura que exista dicho elemento
        self.assertIn("Google", driver.title)
        elemento = driver.find_element(By.NAME, "q")
        elemento.send_keys('Seleium')
        elemento.send_keys(Keys.RETURN) ## RETURN = enter
        time.sleep(5)
        assert"no se encontro el elemento" not in driver.page_source ##Sino encuentra busca en todo el codigo

    ## funcion para cerrar todo
    def tearDown(self):
        self.drver.close()

## con el if cierras la clase y se inicializa dicha class
if __name__ == '__main__':
    unittest.main()