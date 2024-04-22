#este ejercicio nos sirve para scrollear hacia abajo
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class tests(unittest.TestCase):
    def setUp(self):
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
        self.driver = webdriver.Chrome()
    
    def test_scroll_down(self):
        driver = self.driver
        driver.get("https://www.wikipedia.com")
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") #en el numero lo decimos desde que parte de la pantalla nos vamos a ubicar
        time.sleep(5)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()        