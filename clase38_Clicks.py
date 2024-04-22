import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from selenium.webdriver import ActionChains
from time import sleep
import os


class Tests(unittest.TestCase):
    def setUp(self):
        au = UserAgent()
        opts = Options()
        opts.add_argument(f"user-agent={au}")
        driver_path = ChromeDriverManager().install()
        
        if not os.path.exists(driver_path):
            driver_path = ChromeDriverManager().install()
        
        self.driver=webdriver.Chrome(service=Service(driver_path), options=opts)
        
    
    def test_doble_click(self):
        self.driver.get("D:/ESTUDIOS/automation_selenium_with_python/html/navBar_vehiculos.html")
        sleep(3)
        doble_click = self.driver.find_element(By.XPATH, "/html/body/p") #almacena el elemento en esta variable
        sleep(2)
        action = ActionChains(self.driver) #le decimos que vamos a hacer una accion sobre el driver
        action.double_click(doble_click).perform() #aca le decimos que accion, sobre qu elemento y con el perform l decimos que ejecute esa accion
        sleep(3)
        
    def test_click_derecho(self):
        self.driver.get("D:/ESTUDIOS/automation_selenium_with_python/html/navBar_vehiculos.html")
        sleep(3)
        click_derecho = self.driver.find_element(By.XPATH, "/html/body/p[2]") #almacena el elemento en esta variable
        sleep(2)
        action = ActionChains(self.driver) #le decimos que vamos a hacer una accion sobre el driver
        action.context_click(click_derecho).perform() #aca le decimos que haga click derecho, sobre que elemento y con el perform le decimos que ejecute esa accion
        sleep(3)
        
        
    def tearDown(self):
        self.driver.quit()
    
    
if __name__ == "__main__":
    unittest.main()