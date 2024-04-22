from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options #que se utiliza para configurar opciones del navegador Chrome.
from selenium.webdriver.chrome.service import Service #que se utiliza para configurar el servicio del navegador Chrome.
from webdriver_manager.chrome import ChromeDriverManager  #que se utiliza para instalar automáticamente el controlador del navegador Chrome.
from fake_useragent import UserAgent #que proporciona una forma de generar User-Agents aleatorios.


#instanciamos la clase Option() para despues pasarle paremetros a nuestro navegador
opts = Options()


# Crear una instancia de UserAgent que nos genera un ua random
ua = UserAgent()
#User Agent --> es una cadena de texto que me identifica hacia un servidor, e indica la version del navegador que estoy usando
#en el objeto Options vamos a pasarle este User Agent, ya que por default el pseudonavegador de selenium ya tienen uno por defecto el 
#cual es analizado por las paginas web para ver si estamos realizando una extraccion de datos, 
#es especialmente útil en aplicaciones de scraping web donde se necesita evitar la detección de bots
'''
#Obtener un User-Agent aleatorio que simula ser chrome, asi podemos hacer con firefox, edge, random, safari
chrome_user_agent = ua.chrome
print(chrome_user_agent)
'''

opts.add_argument(f"user-agent={ua}") #Agrega un argumento al objeto Options, que establece el User-Agent del navegador Chrome como el User-Agent generado aleatoriamente por fake_useragent.
#opts.add_argument("--headless") #esto para que corra el proceso sin interfaz grafica


driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), #nos detecta la version que tenemos en nuestra maquina e instala el driver correcto
    options=opts
)

driver.get("https://www.airbnb.com")
sleep(3)
ubicacion_anuncio = driver.find_elements(By.CSS_SELECTOR, "[data-testid='listing-card-title']") #buscamos los elementos iguales con el selector de css

for ubicacion in ubicacion_anuncio:
    print(ubicacion.text)
    
sleep(3)