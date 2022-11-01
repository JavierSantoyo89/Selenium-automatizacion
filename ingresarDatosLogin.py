## Manda llamar selenium 
from selenium import webdriver

##Importa el modulo necesario para poder interacturar con los ID o NAME de los campos
from selenium.webdriver.common.by import By

## importa el modulo keys para interactuar con los campos
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
s= Service("C:\driversSelenium\driverChrome\chromedriver.exe")

## Importa el modulo de tiempo para crear un retraso programado
import time

## Manda llamar el driver de chrome
driver =  webdriver.Chrome(service=s)

## Manda llamar el sitio web
driver.get('https://gmail.com')

## ---------- Con esta seccion puedes encontrar e ingresar elcorreo ---------- ##
## Busca el usuario mediante ID
usuario = driver.find_element(By.ID,"identifierId")
## Carga el correo seleccionado
usuario.send_keys("francosantoyo.89@gmail.com")
## Enviar un enter para iniciar
usuario.send_keys(Keys.ENTER)
## Delay, retardo programado
time.sleep(5)
## -------------------------------------------------------------------------- ##

## ---------- Con esta seccion encuentras el campo de password e ingresar datos ---------- ##
## Busca el campo de password por name
password = driver.find_element(By.NAME, "Passwd")
##password = driver.find_element_by_name('Passwd')
password.send_keys('Sam13559274')
password.send_keys(Keys.ENTER)
time.sleep(5)
## -------------------------------------------------------------------------- ##
driver.close() 

