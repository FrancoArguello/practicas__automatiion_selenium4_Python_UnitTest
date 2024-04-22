'''esto nos va a servir para cuando queremos ingresar a un hyperlink que este en un texto corroborar que este este bien escrito '''

import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class throw_tests(unittest.TestCase):
    def setUp(self):
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
        self.driver = webdriver.Chrome()
    def test_automatic_hyprlink(self):
        driver = self.driver
        driver.get("https://es.wikipedia.org/wiki/Argentina")
        time.sleep(5)
        encontrar_link = driver.find_element(By.LINK_TEXT, "país soberano")
        encontrar_link.click()
        time.sleep(5)
        
    def tearDown(self) -> None:
        self.driver.quit()
    
    
    
    
if __name__ == "__main__":
    unittest.main()