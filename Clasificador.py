import pandas
import shutil
import os
import io
import copy

def diferenciador (lista):                                                      #diferencia carpetas de .txt
    textos = []
    for i in lista:
        if ('msg_' or '.txt' or '.TXT') in i:
            textos.append(i)
        else:
            continue
    return textos

def aislador(importante,principio,fin1,fin2):                                   #importante = mensaje ; principio = palabra clave donde empieza ; fin1 = palabra clave final ; fin2 = palabra clave alternativa
    aislado = copy.deepcopy(importante)                                         #copy.deepcopy() genera una copia
    coo1= aislado.index(principio)                                              #busco donde empieza el aislamiento
    for a in range(coo1,-1,-1):                                                 #elimino desde el comienzo del aislamiento hasta el principio del documento
        del aislado [a]
    if fin1 not in aislado:                                                     #busco si el final del aislamiento va a ser con el comienzo del mensaje o si tiene informativo
        coo2 = aislado.index(fin2)
    else:
        coo2 = aislado.index(fin1)
    for a in range(len(aislado),coo2,-1):                                       #elimino desde el final del documento hasta la palabra final
        aislado.pop()
    return aislado                                                              #devuelvo la lista modificada

def ejecutor():                                                                 #diferencia si el radio es ejecutivo o informativo
    TO=aislador(texto_lista,"(TO)","(INFO)","BT")
    ejecutivo=True
    if "DPER" in TO:
        ejecutivo = True
        print ("Este va dirijido a nosotros")
    else:
        ejecutivo = False
        print ("Este es solo informativo")

def carpetas(ruta,nombre):                                                      #en caso de no existir la carpeta, la genera
    ad = os.chdir (ruta)
    if (os.path.isdir(nombre) == False):
        os.mkdir(nombre)


radios = os.listdir("C:/Users/SodaS/OneDrive/Escritorio/Pruebas/PruebaRadio/RADIOS/")
for i in radios:
    archivo_de_texto=open("C:/Users/SodaS/OneDrive/Escritorio/Pruebas/PruebaRadio/RADIOS/"+i,"r")
    texto= archivo_de_texto.read()
    archivo_de_texto.close();
    texto_lista =  texto.split()
    tango = aislador(texto_lista,"(TO)","(INFO)","BT")
    print (ejecutor())
