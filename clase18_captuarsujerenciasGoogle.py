import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Tests(unittest.TestCase):
    
    def setUp(self):
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
        self.driver= webdriver.Chrome()
    
    def test_capturar_sugerencias(self):
        driver = self.driver
        driver.get("https://www.google.com")
        time.sleep(3)
        palabra_busqueda = "seleni"
        search = driver.find_element(By.NAME, "q") #captura el elemento buscado y lo guarda en la variable
        search.send_keys(palabra_busqueda) #en el elemento guardado le envia informacion
        time.sleep(3)
        
        for i in range(1, 11):
            elementos = driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[4]/div[2]/div[1]/div/ul/li["+str(i)+"]/div/div[2]/div[1]/div[1]/span/b") 
            #aca modificamos el xpath proporcionado por la web en donde es que se va a ir modificando segun la opciones que nos vayan presentando
            for elemento in elementos:
                print(f"busqueda sugerdida n° {i}:", palabra_busqueda + elemento.text) 
                #aca concatenamos la palabra que buscamos con el resto que nos sugiere la web asi tiene sentido el resultado obtenido
                #sino solo nos trae las palabras o letras que continuan a lo que nosotros buscamos.
            
                    
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()
