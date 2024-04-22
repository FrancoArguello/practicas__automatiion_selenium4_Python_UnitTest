import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By



class throw_tests(unittest.TestCase):
    
    def setUp(self):
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
        self.driver = webdriver.Chrome()
         
    def test_display_element(self):
        driver = self.driver
        driver.get("https://www.google.com")
        time.sleep(3) #jugamos con estos vaores para dar tiempo a la web a cargar todos los elementos
        display_element= driver.find_element(By.NAME, "btnI")
        print(display_element.is_displayed()) #nos va a retornar un boolean si cargo el elemento, muchas veces demoran en cargar los elementos x mas que se muestre en el front y puede lanzar un false pero si en el siguiente da un true es xq el elemento esta.
        print(display_element.is_enabled()) #nos va retornar un boolean si elemento esta habilitado para su uso
         
    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()