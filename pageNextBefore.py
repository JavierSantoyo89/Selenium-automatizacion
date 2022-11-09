import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class pageNextBefore(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driversSelenium\driverChrome\chromedriver.exe")
    
    def testChengeTabs(self):
        driver = self.driver
        driver.get('http://www.gmail.com')
        time.sleep(3)
        driver.get('http://www.google.com')
        time.sleep(3)
        driver.get('http://www.youtube.com')
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.forward()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
        unittest.main()