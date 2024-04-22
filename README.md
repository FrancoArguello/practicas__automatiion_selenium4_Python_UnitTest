cramos nuestro entorno virtual, para ello instalamos el entorno vitual con pip install virtualenv
desde la consola accedemos a la carpeta Scripts y escribimos activate y le damos enter para ingresar al entorno virtual y poder instalar todo lo que necsitemos sin sobrecargar nuestra computadora.

instalamos selenium usando pip install selenium

---

con pip frezze > requirements.txt creamos nuestro archivo donde vamos a almacenar todas nuestras dependencias que usamos en nuestro entorno vitual

para instalar todas las dependencias juntas al momento de crear un nuevo proyecto usamos
pip install -U -r requirements.txt

---

descargamos e instalamos el driver del buscador con el que vamos a trabajar en este caso el de chrome en https://chromedriver.chromium.org/downloads
y el archivo lo guardamos en una carpeta en el C: con el nombre de driver_chrome

---

creamos una variable de entorno PATH para decirle al sistema donde esta el driver del buscador que estamso utilizando
import os
os.environ['PATH'] += r"rutadeaccesoaldriver"

---

instalamos openCV con pip install opencv-python para trabajar las imagenes y compararlas y capturar la pantalla.

---

instalamos el pyinstaller pip install pyinstaller
crar un archivo .py con el nombre que queremos que tenga el ejecutable
el nombre no debe tener espacios, sino nos va a lanzar un error
recomendable por una cuestion de orden crear una carpeta donde vamos a colocar el archivo .py con el que vamos a trabajar ya que se van a crear varias carpetas nuevas
en la consola nos ubicamos dentro de la carpeta donde alojamos el archivo .py, ahi escribimos pyinstaller nombreDelArchivo.py y le damos enter y se comienza a instalar
todo lo ncesario apra trabajar con esta libreria
en la carpera dist se nos va a crear el .exe que vamos a utilizar como ejecutable
para que nos tire erro con el path cuando ejecutamos el pyinstaller debemos de poner asi pyinstaller --add-binary "C:\driver_chrome\chromedriver.exe";"." nombreDelArchivo.py

---

automatizar una actividad en windows vamos a aplicar lo anterior de pyintaller y vamos a ir a la barra de windows y buscamos
programador de tareas, vamos a crear tarea

---

trabajar con un archivo ini o config para seterar las variables de selenium para ser mas versatiles al momento de invocar algunas caracteristicas del navegador
(clase24)
el .ini nos va a servir para ser llamado desde un archivo .config para poder enviarle la informacion al sistema de por ejemplo que se abran varias paginas
a la vez y s ejecuten diferentes automatizaciones en simultaneo y hacer ciclos, etc.

con los archivos .ini nos ahorramos trabajo de setear toda nuestra app desde cero, asi en cambio la dejamos prearmada y solo modificamos lo que es a la web que queremos ingresar y que
parametros buscar o hacer.

---

instalamos pytesseract

La biblioteca pytesseract facilita el uso de Tesseract OCR en Python al proporcionar una interfaz simple para interactuar con él

Algunos usos comunes de pytesseract incluyen:

1- Extracción de texto de imágenes escaneadas o capturas de pantalla.
2- Automatización de tareas que requieren procesamiento de texto en imágenes, como la lectura de recibos, facturas o documentos.
3- Análisis de imágenes para extraer datos de texto en aplicaciones de visión por computadora.

APARTE DE INSTALAR LA LIBRERIA EN PYTHON HAY QUE INSTALARLA EN WINDOWS YA QUE ES UNA LIBRERIA MUY GRANDE PARA QUE VAYAMOS DEBUGEANDO LOS TEXTOS YA SEA POR IDIOMA O FORMAS.
lo dscargamos de la siguiente pagina la version que necesitemos

aca vamos a usar la tesseract-ocr-w64-setup-v5.0.0-alpha.20191010.exe
C:\Program Files\Tesseract-OCR

## hay muchisimos parametros para debuggear el resultado que nos da la libreria para que sea lo mas fino posible al momento de entender las imagenes.

Installamos html runner con pip install html-testRunner
esta libreria nos va a servir para generar informes en un html al cual se le puede modificar su visual tambien.

---

instalamos un nuevo paquete de webdriver para hacer uso del webdriver de otra forma a la que veniamos realizando hasta el ejercicio 32

pip install webdriver-manager

con este manager no tendremos necesidad de instalar el driver controlador, ya la libreria maneja automaticamente el driver actual del buscador que estamos utilizando y su descarga, ya no es necesario ir instalando nuevas versiones
---

La biblioteca fake-useragent de Python es una herramienta útil para generar User-Agents aleatorios y aleatorios. Los User-Agents son cadenas de texto que los navegadores web envían a los servidores web para identificarse a sí mismos. Esto puede ser útil en diversas situaciones, como web scraping, pruebas de software o para evitar la detección de bots.
pip install fake-useragent


Ejemplo de como decirle el UserAgen que queres que te genere par aun  navegador especifico

from fake_useragent import UserAgent

# Crear una instancia de UserAgent con navegadores específicos
ua = UserAgent(verify_ssl=False)

# Obtener un User-Agent aleatorio que simula ser Firefox
firefox_user_agent = ua.firefox
print(firefox_user_agent)

# Obtener un User-Agent aleatorio que simula ser un navegador móvil
mobile_user_agent = ua.random_mobile
print(mobile_user_agent)


----------------------------------------
pip install undetected_chromedriver

undetected_chromedriver es una biblioteca de Python que proporciona una forma de utilizar el controlador de Chrome (ChromeDriver) de manera "no detectada" o "no detectable" por los sistemas de detección de bots implementados en algunos sitios web.

Cuando automatizas tareas en un navegador web utilizando herramientas como Selenium, a menudo los sitios web pueden detectar que estás utilizando un controlador de navegador automatizado en lugar de un navegador humano normal. Esto puede resultar en la imposibilidad de completar ciertas acciones, redirecciones a páginas de captcha o incluso bloqueos de acceso.

undetected_chromedriver ayuda a evitar este tipo de detecciones al proporcionar una capa de abstracción sobre el controlador de Chrome que incluye técnicas para eludir la detección de bots. Por ejemplo, utiliza técnicas para eliminar las marcas de identificación del controlador, emula comportamientos más humanos (como mover el ratón) y modifica las cadenas de agente de usuario para que coincidan con las de un navegador humano.

En resumen, undetected_chromedriver ayuda a mejorar la eficacia y fiabilidad de tus scripts de automatización al evitar la detección de bots por parte de los sitios web objetivo.

-------------------------------------------------

Instalamos openpyxl para poder trabajar con hojas de calculo con extesion .xlsx

pip install openpyxl

-----------------------------------

