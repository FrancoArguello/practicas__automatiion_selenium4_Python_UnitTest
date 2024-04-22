import os
import time
import unittest
from selenium import webdriver


class tests(unittest.TestCase):
    def setUp(self):
        os.environ['PATH'] += r"C:\driver_chrome\chromedriver.exe"
        self.driver = webdriver.Chrome()
    
    def test_screenshot(self):
        driver = self.driver
        driver.get("https://www.youtube.com")
        time.sleep(3)
        driver.get_screenshot_as_file("D:/ESTUDIOS/automation_selenium_with_python/img/screenshot_youtube.png") #aca le decimos en que ruta guardar la imagen y con que nombre,aca toma un screenshot tal cual como se ve en la pantalla.
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()        