#este ejercicio nos sirve para scrollear hacia abajo
#las cookies son las pequeñas cosas que se guardan para que la pagina cargue mas rapido
#se usa para el auto completado de form y login
import os
import time
import unittest
from selenium import webdriver


class tests(unittest.TestCase):
    def setUp(self):
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
        self.driver = webdriver.Chrome()
    
    def test_scroll_down(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/html/default.asp")
        time.sleep(3)
        
        all_cookies = driver.get_cookies() #aca nos trae todas las cookies, si ponemos .get_cookie("aca tenemos que poner el nombre de la cookie que queremos obtener")
        print(all_cookies)
        
            
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()        