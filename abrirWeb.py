'Mandas llamar Selenium'
from selenium import webdriver

'Mandas llamar al driver'
driver =  webdriver.Chrome(executable_path=r"C:\driversSelenium\driverChrome\chromedriver.exe")

'Mediante el driver mandas llamar a cualquier sitop por medo de .get'
driver.get('http://python.org')

'cierras el driver, de lo contrario se anidaria'
driver.close()