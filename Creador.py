import os
import shutil

def diferenciador (lista):
    textos = []
    for i in lista:
        if ('msg_' or '.txt' or '.TXT') in i:
            textos.append(i)
        else:
            continue
    return textos

nombre = input("Escriba el nombre de la carpeta: ")
ruta = ['LICENCIAS','SUMARIOS','TRASLADOS','CURSOS Y ESCALAFONES','VARIOS']
os.chdir (r'C:/Users/SodaS/OneDrive/Escritorio/Pruebas para el trabajo')
for i in ruta:
    os.chdir (r'C:/Users/SodaS\OneDrive/Escritorio/Pruebas para el trabajo/'+ i)     #me situo
    os.mkdir(nombre)                                                                 #creo
    archivos = os.listdir()                                                          #convierto en lista
    a_mover = diferenciador (archivos)                                               #analizo
    for a in a_mover:                                                                #muevo
        shutil.move( a , nombre)


print ('Carpetas creadas con el nombre de: ',nombre)
