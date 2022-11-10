import time
import cv2 ## Para ver diferencias en imagenes
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class img(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driversSelenium\driverChrome\chromedriver.exe")
    
    def testImgOpenCV(self):
        driver = self.driver
        driver.get('http://www.google.com')
        driver.save_screenshot('img2.png') ## con esto creas un sreenshot
        time.sleep(8)

    def testComparandoImagenes(self):
        img1 = cv2.imread('img1.png')
        img2 = cv2.imread('img2.png')

        diferencia = cv2.absdiff(img1, img2) ## Comparas las imagenes
        imagenGris = cv2.cvtColor(diferencia, cv2.COLOR_BGR2GRAY) ## Convierte la imagen a grises para calcular diferencia
        contours,_ = cv2.findContours(imagenGris,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        for c in contours: ## Para revisar la pisicion de la diferencia
            if cv2.contourArea(c) >= 20:
                posicion_x, posicion_y, ancho,alto = cv2.boundingRect(c)
                cv2.rectangle(img1,(posicion_x,posicion_y),(posicion_x+ancho, posicion_y+alto),(0,0,255),2)


        while(1):
            cv2.imshow('Imagen1', img1)
            cv2.imshow('Imagen2',img2)
            cv2.imshow('diferencias detectadas', diferencia)
            teclado = cv2.waitKey(5) & 0xFF
            if teclado == 27:
                break
        cv2.destroyAllWindows()

if __name__ == '__main__':
    unittest.main()