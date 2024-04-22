import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

class throw_unittest(unittest.TestCase):
    def setUp(self):
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
        self.driver= webdriver.Chrome()
    def test_change_windows(self):
        driver = self.driver
        driver.get("http://www.gmail.com")
        time.sleep(3)
        driver.get("http://www.google.com")
        time.sleep(3)
        driver.get("http://www.youtube.com")
        time.sleep(3)
        
        #aca abrimos pesañas sobre la misma, no es que abrimos nuevas pestañas, cosa de poder trabajar en volver a pagina anterior
        
        driver.back() #para volver a pagina anterior
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.forward() #para volver a la pagina posterior
        time.sleep(3)
        driver.forward() #para volver a la pagina posterior
        time.sleep(3)
        
    def tearDown(self):
        self.driver.close()
        
        
if __name__ == "__main__":
    unittest.main()        