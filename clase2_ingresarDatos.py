from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://universidaddelaciudad.bue.edu.ar/")  #colocamos el sitio web al que queremos ingresar
usuario = driver.find_element("id", "username") #ponemos primero mediante que queremos buscar el elemento y despues el atributo
usuario.send_keys("prueba1") #ponemos que queremos colocar en ese campo
usuario.send_keys(Keys.ENTER) #hacemos que se lleve a cabo un enter

time.sleep(3)

clave = driver.find_element("id", "password")
clave.send_keys("prueba1")
clave.send_keys(Keys.ENTER)

time.sleep(3)