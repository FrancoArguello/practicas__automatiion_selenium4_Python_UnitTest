import cv2 #importamos OpenCv para trabajar con imagenes
import pytesseract


imagen = cv2.imread('img/captcha.png') #lee la imagen y la guarda
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe" #aca va a ir a buscar el ejecutable a donde lo instalamos

texto = pytesseract.image_to_string(imagen) #aca va a avaluar el texto qu aparece en la imagen procesada por opencv
print(texto) #aca nos va a imprimir lo que cree que dice en la imagen. 