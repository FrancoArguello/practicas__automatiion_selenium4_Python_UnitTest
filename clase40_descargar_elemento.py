import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
from webdriver_manager.chrome import ChromeDriverManager 
from time import sleep
import requests

class trow_tests(unittest.TestCase):
    def setUp(self):
        au = UserAgent()
        opts = Options()
        opts.add_argument(f"user-agent={au}")        
        driver_path = ChromeDriverManager().install()
        if not os.path.exists(driver_path):
            driver_path = ChromeDriverManager().install()
        
        # Pasar las opciones al crear la instancia del controlador WebDriver
        self.driver = webdriver.Chrome(service=Service(driver_path), options=opts)
       
    def test_dowload(self):
       
        # Obtener la URL del elemento que queremos descargar --> boton derecho sobre el lemento --> copiar url/direccion
        download_url = "http://127.0.0.1:5500/html/ej_frames/logo_pumas.png"

        # Definir la ubicación de destino para guardar el archivo descargado
        download_path = "D:/ESTUDIOS/automation_selenium_with_python/img/logo_pumas.png"

        # Realizar la solicitud GET para descargar el archivo
        response = requests.get(download_url)

        # Verificar si la descarga fue exitosa
        if response.status_code == 200:
            # Guardar el contenido de la respuesta en un archivo local
            with open(download_path, 'wb') as f:
                f.write(response.content) 
    
    
    def tearDown(self) -> None:
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main()