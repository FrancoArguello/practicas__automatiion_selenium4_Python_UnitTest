import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

class throw_unittest(unittest.TestCase):
    def setUp(self):
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
        self.driver= webdriver.Chrome()
    def test_open_windows(self):
        driver =self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        driver.execute_script("window.open('');") #aca le decimos que abra una nueva pestaña y que la primera pagina va a ser ubicada background entre las comillas del open.
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1]) #con el swirch le decimos que abra otra pantalla, y con el windows_handles le decimos en que pestalla se debe posicionar
        driver.get("http://www.netflix.com") #y aca le decimo que pagina abrir en la pestaña donde nos ubicamos anteriormente
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)
        
    def tearDown(self):
        self.driver.close()
    
if __name__ == '__main__':
    unittest.main()