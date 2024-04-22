import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os




class usando_unittest(unittest.TestCase):
    def setUp(self): #esta funcion nos inicializa los test y aca configuramos el driver
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
        self.driver= webdriver.Chrome()
    def test_search(self):
        driver = self.driver
        driver.get("https://google.com")
        self.assertIn("Google", driver.title) #esto me va a tomar el valor de lo que buscamos y compararlo con el que le pasamos primero, en este caso debe buscar Google en el titulo
        elemento= driver.find_element("name", "q")
        elemento.send_keys("selenium") #aca le indicamos que debe de insertar
        elemento.send_keys(Keys.RETURN)  #el return funciona como el ENTER
        time.sleep(5)
        assert "no se encontro el elemento:" not in driver.page_source #esto evaluar el valor del assert de arriba
    
    def tearDown(self): #esto nos cierra el driver
        self.driver.close()


#con este if le decimos al sistema de donde debe empezar a ejecutar el programa sin necesidad de crear un objeto
if __name__ == "__main__":
    unittest.main()