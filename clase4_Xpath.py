"""
XPath (Lenguaje de Expresión de Caminos) es un lenguaje de consulta utilizado para navegar y seleccionar elementos en un documento XML o HTML. En el contexto de Selenium, XPath se utiliza principalmente para localizar elementos en una página web.

Hay dos tipos principales de XPath que se pueden utilizar para localizar elementos:

XPath Absoluto: Este tipo de XPath comienza desde la raíz del documento y describe la ruta completa hasta el elemento deseado. Por ejemplo, /html/body/div[1]/form/input[1] sería un XPath absoluto que se dirige a la primera casilla de entrada en un formulario dentro de un documento HTML.

XPath Relativo: En contraste con el XPath absoluto, el XPath relativo describe la ruta a un elemento en relación con otro elemento. Este tipo de XPath es generalmente más flexible y menos propenso a errores en comparación con el XPath absoluto. Por ejemplo, //input[@name='q'] sería un XPath relativo que se dirige a cualquier elemento de entrada que tenga el atributo "name" con el valor "q".
"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By #importamos este elemento para poder trabajar con los xpath
import os
import time

class usando_unittest(unittest.TestCase):
    def setUp(self):
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
        self.driver= webdriver.Chrome()
        
    def test_search_xpath(self):
        driver = self.driver
        driver.maximize_window() #nos muestra la pantalla maximizada
        driver.get("http://www.google.com")
        time.sleep(3)
        search_xpath = driver.find_element(By.XPATH , '//*[@name="q"]') #el Xpath siempre se debe escribir con comillas simples
        search_xpath.send_keys("selenium",Keys.ARROW_DOWN)#nos muestra las opciones de busqueda y se ubica en la primera opcion
        search_xpath.send_keys(Keys.RETURN)  #el return funciona como el ENTER
        time.sleep(3)
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()    
        
        