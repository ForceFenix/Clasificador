import io
import os

archivo_de_texto=open("C:/Users/SodaS/OneDrive/Escritorio/Pruebas/PruebaRadio/RADIOS/msg_416441.txt","r")
texto= archivo_de_texto.read()
archivo_de_texto.close();
enter = texto.replace(" X ", "\n")
print(enter)
print(enter.split("\n",))
