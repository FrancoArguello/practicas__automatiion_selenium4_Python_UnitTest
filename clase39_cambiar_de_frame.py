import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from webdriver_manager.chrome import ChromeDriverManager 
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class trow_tests(unittest.TestCase):
    def setUp(self):
        au = UserAgent()
        opts = Options()
        opts.add_argument(f"user-agent={au}")
        prefs = {"download.default_directory" : "D:/ESTUDIOS/automation_selenium_with_python/img"}
        opts.add_experimental_option("prefs", prefs)
        
        #con esto hacemos que no muestre el cartel de que el Chrome esta controlado por un software de automatizacion
        opts.add_experimental_option("excludeSwitches", ["enable-automation"]) 
        
        driver_path = ChromeDriverManager().install()
        
        if not os.path.exists(driver_path):
            driver_path = ChromeDriverManager().install()
        
        self.driver=webdriver.Chrome(service=Service(driver_path), options=opts)
       
    def test_dowload(self):
        driver = self.driver
        driver.get("D:/ESTUDIOS/automation_selenium_with_python/html/ej_frames/index.html")
        sleep(3)
        
        driver.switch_to.frame(0)  # Cambiar al primer frame
        input = driver.find_element("id", "texto_ingresado")
        input.send_keys("Estoy en el primer Frame")
        input.send_keys(Keys.ENTER)
        sleep(3)
        
        driver.switch_to.default_content()  # Salir del frame actual a la web principal
        driver.switch_to.frame(1)  # Cambiar al segundo frame
        
        input2 = driver.find_element("id", "texto_ingresado2")
        input2.send_keys("cambio exitoso de frame")
        input2.send_keys(Keys.ENTER)
        sleep(3)
    
    
    
    def tearDown(self) -> None:
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main()