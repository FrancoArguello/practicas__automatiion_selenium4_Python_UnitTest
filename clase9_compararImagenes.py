''' Vamos a comparar imagenes con Selenium vamos a hacer captura de pantallas y con OpenCV vamos a comparar imagenes'''

import os
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import cv2
import time

class throw_unittest(unittest.TestCase):
    def setUp(self):
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
        self.driver = webdriver.Chrome()
        
    def test_use_opencv(self):
        driver = self.driver
        driver.get("http://www.google.com")
        driver.save_screenshot('img/img2.png') #usamos para sacar un screenshot solo de la pantalla, no nos toma pestañas ni barra de windows
        time.sleep(3)

        #aca una vez cargada la pagina y hecho el screenshot va a comenzar a comparar las imagenes
        img1 = cv2.imread('img/con_cartel.png') #usamos esto para leer la imagen
        img2 = cv2.imread('img/img2.png')
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0])) #con esto redimencianamos la imagen que va a tomar el sistema en escala a la imagen que le proporcionamos para comparar  el 1 representa la anchura y el 0 representa la altura
        
        diferencia = cv2.absdiff(img1, img2) #Es una función de OpenCV que calcula la diferencia absoluta entre dos imágenes pixel por pixel
        imagen_gris = cv2.cvtColor(diferencia, cv2.COLOR_BGR2GRAY) #aca pasamos las imagenes a una escala de grises para que sea ams rapido procesar la imagen y encontrar las diferencias
        contours,_ = cv2.findContours(imagen_gris, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #findcontour almacena los contornos encontrados, retr_external encuentra y almacena los controles externos y chain_approx_simple utiliza una aproximacion basica a la figura real del controrno del elemento.
        
        for c in contours:
            if cv2.contourArea(c) >=20: #aca le decimos que capture los valores en donde la diferencia de color es mayor a 20 segun la escala, cuanto mas chico es mas preciso pero mas propenso a errores
                posicion_x, posicion_y, ancho, alto = cv2.boundingRect(c) #crea un rectangulo de color
                cv2.rectangle(img1,(posicion_x, posicion_y),(posicion_x + ancho, posicion_y + alto), (0,0,255),2)
        
        while(1): #asi creamos un bucle infinito hasta que se lo detiene
            cv2.imshow('imagen1', img1)
            cv2.imshow('imagen2', img2)
            cv2.imshow('diferencias_detectadas', diferencia)
            teclado = cv2.waitKey(5) & 0xFF
            if teclado == 27: #Esta línea verifica si la tecla presionada es la tecla ESC (cuyo código ASCII es 27).
                break
        
        cv2.destroyAllWindows() #cierra todas las ventanas abiertas.
    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
