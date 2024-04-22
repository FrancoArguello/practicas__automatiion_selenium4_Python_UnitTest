import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains #sirve para simular un movimiento del mause, pero no se ve el movimiento del cursor



class throw_tests(unittest.TestCase):
    
    
    def setUp(self):
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
        self.driver = webdriver.Chrome()
    
    def test_use_hover(self):
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        element = driver.find_element(By.XPATH, "//*[text()='Privacidad']") #busca el elemento con es tecto visible
        
        hover = ActionChains(driver).move_to_element(element) #mueve el curso al elemento
        hover.perform() #para que ejecute la accion, incluso podemos notar que el cursor cambia de forma que esto nos indica que esta iniciada la ejecucion
        time.sleep(5)
    # def tearDown(self):
    #     self.driver.quit()    
    
        
if __name__ == "__main__":
    unittest.main()