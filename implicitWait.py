##Implicitwait = es como el time.sleep espera cieto tiempo para iniciar, en segundos

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

class implicitwait(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driversSelenium\driverChrome\chromedriver.exe")
    
    def testImplicitWait(self):
        driver = self.driver
        driver.implicitly_wait(5) #segundos
        driver.get('http://www.google.com')
        mydinamicElement = driver.find_element(By.NAME,'q')
    
if __name__ == '__main__':
    unittest.main()