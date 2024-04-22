import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



class throw_test(unittest.TestCase):
    def setUp(self):
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
        self.driver = webdriver.Chrome()
    
    def test_click(self):
        driver = self.driver
        driver.get('https://proyecto-barberia.netlify.app/contacto')
        time.sleep(5)
        radio_bt= driver.find_element(By.XPATH, "//*[@id='radio-telefono']")
        radio_bt.click()
        time.sleep(3)   
        radio_bt = driver.find_element(By.XPATH, "//*[@id='radio-email']")
        time.sleep(3)
        radio_bt.click()
        time.sleep(3)
        
    def tearDown(self):
        self.driver.quit()
        
        
if __name__ == "__main__":
    unittest.main()
        
        