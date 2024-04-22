import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
import os
from time import sleep
from selenium.webdriver import ActionChains


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
    
    
    def test_mover_cursor(self):
        self.driver.get("D:/ESTUDIOS/automation_selenium_with_python/html/navBar_vehiculos.html")
        sleep(3)
        mouse_mov = self.driver.find_element(By.XPATH, "//*[@id='navbarNav']/ul/li[1]/a")
        mouse_mov2 = self.driver.find_element(By.XPATH, "//*[@id='navbarDropdown']")
        mouse_mov3 = self.driver.find_element(By.XPATH, "//*[@id='navbarNav']/ul/li[2]/div/a[3]")
        movimiento = ActionChains(self.driver)
        movimiento.move_to_element(mouse_mov).move_to_element(mouse_mov2).click()
        sleep(3)
        movimiento.move_to_element(mouse_mov3).click().perform()
        sleep(3)
        
        
        
        
    def tearDown(self):
        self.driver.quit()
    
    
    
if __name__ == "__main__":
    unittest.main()