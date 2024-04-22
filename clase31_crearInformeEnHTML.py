import HtmlTestRunner #libreria para que nos cree el informe de resulado de los tests en un HTML
import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Tests(unittest.TestCase):
    def setUp(self):
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
        self.driver= webdriver.Chrome()
        
    def test_busqueda(self):
        self.driver.get("https://www.google.com")
        self.search = self.driver.find_element(By.NAME, "q")
        self.search.send_keys("selenium")
        self.search.submit()
        time.sleep(3)
        
    def test_scroll_down(self):
        driver = self.driver
        driver.get("https://www.wikipedia.com")
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        
    def test_automatic_hyprlink(self):
        driver = self.driver
        driver.get("https://es.wikipedia.org/wiki/Argentina")
        time.sleep(5)
        encontrar_link = driver.find_element(By.LINK_TEXT, "país soberano")
        encontrar_link.click()
        time.sleep(5)
        
        
    def tearDown(self):
        self.driver.quit()
        
        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:/ESTUDIOS/automation_selenium_with_python/html/Informe_test")) #le decimos donde crear los archivos y con que nombre
    
    #lo colocamos en la llamada de inicip del proceso para que sepa que al final nos debe generar el reporte en un html, si lo colocamos como una
    #funcion dentro del proceso lo va a tomar como un test mas y no nos va a generar el archivo