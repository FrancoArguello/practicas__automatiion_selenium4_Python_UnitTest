import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent

class Tests(unittest.TestCase):
    def setUp(self) -> None:
        opts = Options()
        ua = UserAgent()
        opts.add_argument(f"user-agent={ua}")
        opts.add_argument("--headless") #para que se corra el proceso en segundo plano
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=opts
        )
    def test_assert_equals(self):
        self.driver.get("https://www.google.com")
        titulo_pagina = self.driver.title #obtenemos el valor del titulo de la pagina
        self.assertEqual("google", titulo_pagina, "no coincide el titulo")
        #primero pasamos que queremos que compare, segundo con que queremos que compare, y tercero le pasamos 
        #un mensaje de error en el caso de que no haya coincidencia
        
        
        #si hay coincidencia nos va a decir ok 
        #si no hay concidencia te va a decir los valores encontrados y el mesj de error
        
        
    def tearDown(self) -> None:
        self.driver.quit()
    

if __name__ == "__main__":
    unittest.main()