import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class abriendoVentanas(unittest.TestCase):

    def setUp(self):
       self.driver = webdriver.Chrome(executable_path=r"C:\driversSelenium\driverChrome\chromedriver.exe")
    
    def testVentana(self):
        ## Carga la primera pestaña
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        ## -------------------------
        ## Carga la segunda pestaña
        driver.execute_script("window.open('');")
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        driver.get('http://www.facebook.com')
        time.sleep(3)
        ## -------------------------
        ## Regresa a la primera pestaña
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()