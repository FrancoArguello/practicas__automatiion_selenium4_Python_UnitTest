import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class Tests(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") #"Headless" se refiere a la ejecución de un navegador web sin una interfaz gráfica visible
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
        self.driver= webdriver.Chrome( options = chrome_options) #desde selenium 4 se utiliza el parametro option y a sa le asignamos el valor del argumento
    
    def test_manejando_tablas(self):
        driver = self.driver
        driver.get("https://prjm.site/contacto.html")
        time.sleep(3)
        
        
        #asi accedemos a los titulos de la tabla
        titulos = driver.find_element(By.XPATH, "/html/body/main/table/thead").text
        print(titulos)
        
        #aca vamos a empezar a trabajar con las columnas y las filas
        rows = len(driver.find_elements(By.XPATH, "/html/body/main/table/tbody/tr")) #aca le decimos que nos capture la cantidad de los tr
        col = len(driver.find_elements(By.XPATH, "/html/body/main/table/tbody/tr[1]/td")) #aca le decimos que nos capture  la cantiadad de los td desde el tr[1] para que nos nos traiga los titulos que ya le pedimos arriba
        
        #print(rows) #para saber cantidad de filas
        #print(col)  #para saber cantidad de columnas
        #nos va a servir para delimitar nuetro for asi no se rompe el programa
        
        for i in range(1, rows +1):
            
            for j in range(1, col+1):
                info = driver.find_element(By.XPATH, "/html/body/main/table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
                print(info, end=' ') #con el end le seteamos la separacion o que queremos que fijere entre la informacion
            print()
            
        
    
    
    def tearDown(self) -> None:
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()