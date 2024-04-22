import configparser #nos sirve para parsear una configuracion para despues grabarla en un archivo con la extension que querramos

#import os
#print("Directorio de trabajo actual:", os.getcwd()) #con esto podemos saber en que ruta de archivo estamos trabajando

configuracion = configparser.ConfigParser()
#aca colocamos las  secciones que va a tener nuestro .ini y despues con el = le asignamos la informacion a la seccion
configuracion['General'] = {'chrome':'C:/driver_chrome/chromedriver.exe'} #aca le pasamos la unicacion de los diferentes Driver de navegadores que trabajemos
configuracion['Paginas'] = {'page' : 'https://www.google.com'}

with open('configuracion.ini', 'w') as archivoconfig: #aca le decimos que si no existe el archivo que lo cree y si existe que lo reescriba
    configuracion.write(archivoconfig)