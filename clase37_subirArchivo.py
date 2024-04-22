import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
import os
from time import sleep
import HtmlTestRunner

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
    
    def test_subir_archivo(self):
        self.driver.get("D:/ESTUDIOS/automation_selenium_with_python/html/input_archivo.html")
        sleep(3)
        #buscamos el input por ID
        input_file = self.driver.find_element(By.ID, "upload-image")
        #le enviamos el archivo que queremos subir
        input_file.send_keys("D:\\ESTUDIOS\\automation_selenium_with_python\\img\\captcha.png")
        sleep(4)

    def tearDown(self):
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:/ESTUDIOS/automation_selenium_with_python/html/Informe_test"))