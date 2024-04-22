#como crear un archivo .exe para programar una tarea de windows
#hay que instalar el modulo de pyinstaller para crear ejecutables con python
# para que nos tire error con el path cuando ejecutamos el pyinstaller debemos de poner asi pyinstaller --add-binary "C:\driver_chrome\chromedriver.exe";"." ejecutable.py
import os
from selenium import webdriver
import time
import unittest

class tests(unittest.TestCase):
    def setUp(self):
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
        self.driver = webdriver.Chrome()

    def test_basic(self):
        driver = self.driver
        driver.get("http://python.org")
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
        
        
if __name__ == "__main__":
    unittest.main()