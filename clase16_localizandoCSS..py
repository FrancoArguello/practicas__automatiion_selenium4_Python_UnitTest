import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class tests(unittest.TestCase):
    def setUp(self):
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
        self.driver = webdriver.Chrome()
    
    def test_search_select_css(self):
        driver = self.driver
        driver.get("http://20.150.223.53/contacto.html")
        time.sleep(3)
        content = driver.find_element(By.CSS_SELECTOR, "a")  #aca colocamos el selector del css del elemnto que estamos buscando
        content.click()
        time.sleep(5)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()        