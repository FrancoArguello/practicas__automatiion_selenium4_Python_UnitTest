import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
import os
from time import sleep


class Tests(unittest.TestCase):
    
    def setUp(self) -> None:
        ua = UserAgent()
        opts = Options()
        opts.add_argument(f"user-agent={ua}")
        
        '''Para no instalar reiteradamente el driver creamos este if para corroborar si esta instalado 
        y si coincide la version instalada con la actual'''
        
        # Obtener la ruta del controlador
        driver_path = ChromeDriverManager().install()
        #print(driver_path) #nos imprime la ruta de acceso al driver
        
        # Verificar si el controlador ya está instalado
        if not os.path.exists(driver_path):
            # Si no está instalado, instalar el controlador
            driver_path = ChromeDriverManager().install()
        
        # Crear una instancia del navegador Chrome
        self.driver = webdriver.Chrome(service=Service(driver_path), options=opts)
    
    
    def test_manejando_pestanas(self):
        self.driver.get("D:/ESTUDIOS/automation_selenium_with_python/html/login.html")
        sleep(3)
        next_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/a")
        next_button.click()
        print(self.driver.current_window_handle) # imprime en la consola el identificador de la ventana actual (window handle) en la que se encuentra el controlador de Selenium
        sleep(3)
        
        handles = self.driver.window_handles
        
        
        #con esto hacemos que por consola nos imprima el titulo de todas las pestañas
        for handle in handles:
            self.driver.switch_to.window(handle)
            print(self.driver.title)
            
            
        if len(handles) > 1: #verifica la cantidad de pestañas abiertas
            self.driver.switch_to.window(handles[1]) #aca le decimos en que pestaña queremos que se ponga el foco
            
        titulo_pagina = self.driver.title #obtenemos el valor del titulo de la pagina sobre la cual esta el foco
        self.assertEqual("Create Accounte", titulo_pagina, "no switcheo correctamente") #comparamos si el titulo es el correcto
  
  
    def tearDown(self):
        self.driver.quit()
    
    
    
if __name__ == "__main__":
    unittest.main()
