import time
import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
#necesitamos esto para trabajar con las notificaciones emergentes
#ya qu no podemos acceder a ese elemento ya que es info que trabaja por detras enbebidos en el sistema 

class Tests(unittest.TestCase):
    def setUp(self):
        #instanciamos Options() para trabajar con este elemento
        options = Options()
        #valor de argumentos(1 permite, 2 bloquea las notificaciones)
        prefs = {"profile.default_content_setting_values.notifications": 1} #aca colocamos el argumento de acetacion que vamos a enviar
        options.add_experimental_option("prefs", prefs) 
        
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
        self.driver= webdriver.Chrome(options = options) #aca le pasamos al driver el parametro de trabajo
    def test_notifications(self):
        driver = self.driver
        driver.get("D:/ESTUDIOS/automation_selenium_with_python/html/notificaciones.html")
        time.sleep(3)
             
    def tearDown(self):
        self.driver.quit()
        
        
if __name__ == "__main__":
    unittest.main()