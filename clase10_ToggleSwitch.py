import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class throw_unittest(unittest.TestCase):
    
    def setUp(self):
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
        self.driver = webdriver.Chrome()
    
    def test_using_toggle(self):
        driver = self.driver
        driver.get("https://mui.com/material-ui/react-toggle-button/") #"busca la pagina"
        time.sleep(3)
        toggle = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[13]/div[2]/div/button[1]") #nos captura el lemento n esta variable, el xpath hay que cambiarle las "" por ''
        toggle.click()
        time.sleep(3)
        toggle.click()
        time.sleep(3)
        
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()
    