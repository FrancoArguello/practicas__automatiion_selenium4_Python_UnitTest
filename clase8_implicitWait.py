import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class throw_unittest(unittest.TestCase):
    def setUp(self):
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
        self.driver= webdriver.Chrome()
        
        
    def test_use_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5) #aca le decimos cuantos segudos maximos debe esperar para lanzar el proceso
        driver.get("http://www.google.com")
        my_dinamic_element=driver.find_element(By.NAME,"q") #con esto le decimos que espere a que apareza este elemento y cuando lo encuentra lo almacene en esta variable, nos sirve en el caso que haya un carrusel de imagenes etc, que va cambiando 
         
        
    def tearDown(self):
        self.driver.quit()
        
        
if __name__ == "__main__":
    unittest.main()