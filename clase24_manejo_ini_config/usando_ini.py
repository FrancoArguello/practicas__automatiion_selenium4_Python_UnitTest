import unittest
import os
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Tests(unittest.TestCase):
    def setUp(self):
        configuracion = configparser.ConfigParser()
        configuracion.read('configuracion.ini') #aca le decimos que archivo debe leer
        configuracion.sections() #aca vamos a obtener la informacion de las secciones
        obtener_explorador = configuracion["General"]["chrome"] #aca le decimos que driver de navegador queremos que nos traiga
        self.page = configuracion["Paginas"]["page2"] #capturamos en esta variable el valor para usarlo despues en otras funciones
        
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe" + obtener_explorador  
        self.driver = webdriver.Chrome()  # Inicializa el controlador Chrome
        
    def test_use_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get(self.page)
        myDynamicElement = driver.find_element(By.NAME, "q") #le ponemos el MyDinamicElement para hacer referencia que puede ser cualquier lemento
        time.sleep(3)
        
    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()