import os 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert #para trabajar con los alert 


os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
driver= webdriver.Chrome()
driver.get("D:\ESTUDIOS/automation_selenium_with_python/html/alert.html")
time.sleep(3)
alert_simple = driver.find_element(By.NAME, "alert")
alert_simple.click()
time.sleep(3)
alert_simple = Alert(driver) #aca instanciamos a la clase Alert, que nos va a servir para cambiar el foco al Alert que nos figura en pantalla, antes se usaba el driver.switch_to_alert()
alert_simple.dismiss() #cierra/cancel automaticamente el popUp por default sin importar el idioma o texto que figure para salir
time.sleep(3)
driver.quit()