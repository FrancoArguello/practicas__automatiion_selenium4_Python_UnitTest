import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class throw_test(unittest.TestCase):
    def setUp(self):
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
        self.driver = webdriver.Chrome()
        
    def test_use_select(self):
        driver = self.driver
        driver.get("https://proyecto-barberia.netlify.app/contacto")
        select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='contact-div']/form/fieldset[2]/select"))
)
        opciones = select.find_elements(By.TAG_NAME, "option")
        time.sleep(3)
        
        for option in opciones:
            print("los valores son: %s" % option.get_attribute("value"))
            option.click()
            time.sleep(3)
        seleccionar = Select(driver.find_element(By.TAG_NAME, "select"))
        seleccionar.select_by_visible_text("Tarde") #usamo select_by_visible_text cuando la etiqueta no tiene el atributo value,en ese caso usamos select_by_value()
        time.sleep(10)
        
        
        
    def tearDown(self):
        self.driver.quit()
        
        
if __name__ == "__main__":
    unittest.main()