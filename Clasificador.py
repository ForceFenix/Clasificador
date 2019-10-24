import pandas
import shutil
import os
import io

def aislador(importante,principio,fin1,fin2):                                   #importante = mensaje ; principio = palabra clave donde empieza ; fin1 = palabra clave final ; fin2 = palabra clave alternativa
    coo1= importante.index(principio)                                           #busco donde empieza el aislamiento
    for a in range(coo1,-1,-1):                                                 #elimino desde el comienzo del aislamiento hasta el principio del documento
        del importante [a]
    if fin1 not in importante:                                                  #busco si el final del aislamiento va a ser con el comienzo del mensaje o si tiene informativo
        coo2 = importante.index(fin2)
    else:
        coo2 = importante.index(fin1)
    for a in range(len(importante),coo2,-1):                                    #elimino desde el final del documento hasta la palabra final
        importante.pop()
    return importante                                                           #devuelvo la lista modificada

def ejecutor(TO):
    ejecutivo=True
    if "DPER" in TO:
        ejecutivo = True
    else:
        ejecutivo = False
    return ejecutivo


archivo_de_texto=open("C:\\Users\SodaS\OneDrive\Escritorio\Pruebas\PruebaRadio\RADIOS\msg_416441.txt","r")
texto= archivo_de_texto.read()
archivo_de_texto.close();
texto_lista =  texto.split()
tango_oscar=aislador(texto_lista,"(TO)","(INFO)","BT")
print(tango_oscar)
print(ejecutor(tango_oscar))
