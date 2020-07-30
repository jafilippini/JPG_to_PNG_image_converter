""" Conversor de imágenes .jpg a .png enforma masiva.
linea de comando:   python .\JPGtoPNGConverter_v1.py Source_dir Destination_dir
  
  Source_dir: directorio que contiene archivos .jpg (entre otras cosas)
  Destination_dir: directorio en el que quedarán los files .png_file

ejemplo:  python .\JPGtoPNGConverter_v1.py Imagenes New_dir
donde:

    Imagenes: es un directorio ubicado en el mismo directorio que el archivo JPGtoPNGConverter_v1.py
    New_dir: es el directorio de destino, que será creado si no existe, y si existe se escribe en él


el programa consulta ancho y alto deseados para imágenes .png, una vez hecho ésto tomará del directorio Source_dir todos los archivos .jpg
y los convertirá a .png dejándolos en el directorio que se defina como Destination _dir """

import sys
import os
from PIL import Image,ImageFilter


def grab_args(pos):
    # retorno el valor de cada argumento pasado en la linea de comando en función de la posición deseada
    return sys.argv[pos]


def check_dest_exist(dest):
# chequeo si el directorio de destino existe
    return os.path.isdir(dest)


def create_dest(dest):
# creo un directorio de destino
    os.mkdir(dest)
    return


def sublist_of_stringlist(str_target, str_list):
# devuelve una sublista con los elementos de una lista de strings (str_list) que contienen un string (str_target)
    jpg_list = []
    for index in str_list:
        if index.find(str_target) > 0:
            jpg_list.append(index)
    return jpg_list


# Obtengo los argumentos
source_dir ='.\\'+ grab_args(1)

dest_dir ='.\\'+ grab_args(2)

# chequeo si el directorio de destino existe y si no existe lo creo
if not check_dest_exist(dest_dir):
    create_dest(dest_dir)

# obtengo la lista de archivos .jpg del directorio de origen
jpg_list = sublist_of_stringlist('.jpg', os.listdir(source_dir))

#Consulto sobre el ancho y alto de los files .png
ancho=int(input('Ancho de imagen .png:'))
alto=int(input('Alto de imagen .png:'))

# recorro los archivos .jpg, convierto sus nombres a .png y los grabo como .png
for jpg_file in jpg_list:
    jpg_img = Image.open(source_dir + '\\' + jpg_file)
    resized=jpg_img.resize((ancho,alto))
    png_file=jpg_file.replace('jpg','png')
    #jpg_img.save(dest_dir+'\\'+png_file, 'png')
    resized.save(dest_dir+'\\'+png_file, 'png')

