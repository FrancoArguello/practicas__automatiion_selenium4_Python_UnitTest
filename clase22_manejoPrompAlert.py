import time
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert #para trabajar con los alert 
from selenium.webdriver.common.keys import Keys


class Tests(unittest.TestCase):
    def setUp(self):
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
    driver= webdriver.Chrome()
    
    def test_use_prompt_alert(self):
        driver = self.driver
        driver.get("D:\ESTUDIOS/automation_selenium_with_python/html/promptAlert.html")
        time.sleep(3)
        alert = driver.find_element(By.NAME, "prompt_alert")
        alert.click()
        alert = Alert(driver) #aca instanciamos a la clase Alert, que nos va a servir para cambiar el foco al popUp que nos figura en pantalla, antes se usaba el driver.switch_to_alert()
        alert.send_keys("Franco") #inserta el nombre Franco
        #alert.send_keys("") #envia una cadena vacia 
        #alert.accept() #nos va a hacer click en aceptar
        alert.dismiss() #da en cancel
        time.sleep(3)
        
    def tearDown(self):
        self.driver.quit()
        
        
if __name__ == "__main__":
    unittest.main()