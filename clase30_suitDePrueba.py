#estructura correcta que debemos de seguir para crear nuestro suit de prueba

#llamamos a todas las dependencias que vamos a utilizar
import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



#inicializamos la clase que va a contener a todas las pruebas
#la podemos llamar como querramos
class Tests(unittest.TestCase):
    
    #inicar la clase con una funcion setUp() donde vamos a setear nuestro
    #driver que vamos a utilizar para controlar algun motor de busqueda
    #Chrome, Mozilla, Firebox, IE, etc.
    #aca vamos a ubicar todas nuestras variables de iniciacion en este caso seria self.driver
    def setUp(self):
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
        self.driver= webdriver.Chrome()
        
     #Creamos todos los testCass que vayamos a utilizar o necesitar
     #SIEMPRE DEBEN COMENZAR CON LA PALABRA test para que sean reconocidos por UnitTest   
    def test_busqueda(self):
        #aca para no declarar una nueva variable podemos usar el self.driver directamente
        self.driver.get("https://www.google.com")
        self.search = self.driver.find_element(By.NAME, "q")
        self.search.send_keys("selenium")
        self.search.submit()
        time.sleep(3)
        
    def test_scroll_down(self):
        driver = self.driver
        driver.get("https://www.wikipedia.com")
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") #en el numero lo decimos desde que parte de la pantalla nos vamos a ubicar
        time.sleep(5)
        
    def test_automatic_hyprlink(self):
        driver = self.driver
        driver.get("https://es.wikipedia.org/wiki/Argentina")
        time.sleep(5)
        encontrar_link = driver.find_element(By.LINK_TEXT, "país soberano")
        encontrar_link.click()
        time.sleep(5)
        
        
    #siempre al final es recomendable crear esta funcion que lo que va a hacer es limpiar nuestras variables, y cerrar todos los procesos ejecutados para no tener varios
    #driver abiertos y utilizar recursos de manera innecesaria
    def tearDown(self):
        self.driver.quit()
        
        
# setUp() y tearDown() unittest ya las reconoce como variables de inicializacion y variables de finalizacion automaticamente por eso
# no hace falta colocarles la palabra test adelante del nombre de la funcion.

# si no agregamos este if no van a correr los test
#este fragmento de código permite que las pruebas unitarias definidas en el mismo
# archivo se ejecuten cuando el archivo se ejecuta como un programa independiente. 
# Esto es útil para probar y verificar el comportamiento de diferentes partes de tu código de manera automatizada.       
if __name__ == "__main__":
    unittest.main()