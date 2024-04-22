import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class throw_unittest(unittest.TestCase):
    def setUp(self):
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
        self.driver= webdriver.Chrome()
    
    def test_use_explicit_wait(self):
        driver = self.driver
        driver.get("http://www.google.com")
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
            #aca le decimos con el driverWait que haga 10 intentos sobre el driver de ejecutar la accion ordenada, y con el until le decimos que espere hasta que se cargue la pagina y este el elemento localizado con el nombre q
        finally:
            driver.quit()
        
        
    def tearDown(self):
        self.driver.quit()
         
    
if __name__ == "__main__":
    unittest.main()