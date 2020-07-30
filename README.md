# JPG_to_PNG_image_converter
.jpg files to .png files massive converter

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
