import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from fake_useragent import UserAgent
import os
from selenium.webdriver.common.keys import Keys
import time


class Tests(unittest.TestCase):
    def setUp(self):
        au = UserAgent()
        opts = Options()
        opts.add_argument(f"user-agent={au}")   
        #con esto hacemos que no muestre el cartel de que el Chrome esta controlado por un software de automatizacion
        opts.add_experimental_option("excludeSwitches", ["enable-automation"])      
        driver_path = ChromeDriverManager().install()
        if not os.path.exists(driver_path):
            driver_path = ChromeDriverManager().install()
        
        # Pasar las opciones al crear la instancia del controlador WebDriver
        self.driver = webdriver.Chrome(service=Service(driver_path), options=opts)
       
    def test_llenar_formulario(self):
        driver = self.driver
        driver.get("D:/ESTUDIOS//automation_selenium_with_python/html/login.html")
        time.sleep(3)
        
        
        #ste for nos permite insertar varios datos en varios campos e irle asigando un valor al momento de dividirlo con el split()
        with open(r'D:/ESTUDIOS/automation_selenium_with_python/static/datos.txt') as file:
            for i, line in enumerate(file):
                usuario = (line)
                sep = ","
                dividir = usuario.split(sep)
                
                try:
                    got_data = dividir[1] #es la linea de datos encontrados
                    username = dividir[0] #es el primer elemento resultante de la division --> username
                    password = dividir[1] # es el segundo elemento --> password
                except IndexError:
                    got_data = "null"
                    
                driver.find_element(By.ID,"username").send_keys(username)
                print(username)
                time.sleep(3)
                driver.find_element(By.ID, "password").send_keys(password)
                print(password)
                time.sleep(5)
                driver.find_element(By.ID, "login").click()
                time.sleep(3)
                
                # Borra los datos de los campos de texto
                #driver.find_element(By.ID,"username").clear()
                #driver.find_element(By.ID, "password").clear()
        
        file.close()
    def tearDown(self):
        self.driver.quit()
        
        
if __name__ == "__main__":
    unittest.main()