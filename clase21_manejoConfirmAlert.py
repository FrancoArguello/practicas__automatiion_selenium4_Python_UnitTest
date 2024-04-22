import os 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert #para trabajar con los alert 


os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
driver= webdriver.Chrome()
driver.get("D:\ESTUDIOS/automation_selenium_with_python/html/confirmAlert.html")
time.sleep(3)
confirm_alert = driver.find_element(By.NAME, "confirm_alert")
confirm_alert.click()
time.sleep(3)
confirm_alert = Alert(driver) 
#aca instanciamos a la clase Alert, que nos va a servir para cambiar el foco al popUp 
#que nos figura en pantalla, antes se usaba el driver.switch_to_alert()
confirm_alert.accept() #nos va a hacer click en aceptar
time.sleep(3)
driver.quit()