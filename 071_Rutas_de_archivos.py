#!/usr/bin/env python3

# Windows file directory
# C:\my-directory\target-file.txt

# Windows file directory written in Python
# C:/my-directory/target-file.txt.

# #Windows file directory
# C:\\my-directory\\target-file.txt

# #CWD command:
# os.getcwd()

# #CWD command for external files:
# outputs['current_directory_before'] = os.getcwd()

import os  # Importa el módulo os para interactuar con el sistema operativo
import datetime  # Importa el módulo datetime para trabajar con fechas y horas

# Comprueba si el archivo "novel.txt" existe
print(os.path.exists("novel.txt"))  # Imprime True si el archivo existe, False en caso contrario
# Comprueba si el archivo "declaration.txt" existe
print(os.path.exists("declaration.txt"))  # Imprime True si el archivo existe, False en caso contrario

print("-------------------------------------------------------")

# Obtiene el directorio de trabajo actual
# os.remove("novel.txt")  # Elimina el archivo "novel.txt" si existe (comentado)

print("--------------------------------------------------------")

# Obtiene el directorio de trabajo actual
# os.remove("novel.txt")  # Elimina el archivo "novel.txt" si existe (comentado)
# os.remove("novel.txt")  # Elimina el archivo "novel.txt" si existe (comentado)
print("---------------------------------------------------------")

# os.rename("novel.txt", "novel.txt.bak")  # Renombra el archivo "novel.txt" a "novel.txt.bak" si existe (comentado)
# os.rename("novel.txt.bak", "novel.txt")  # Renombra el archivo "novel.txt.bak" a "novel.txt" si existe (comentado)

print("---------------------------------------------------------")

tam = os.path.getsize("spider.txt")  # Obtiene el tamaño del archivo "spider.txt" en bytes
print(tam)  # Imprime el tamaño del archivo en bytes

mod = os.path.getmtime("spider.txt")  # Obtiene la fecha de la última modificación del archivo "spider.txt" en segundos desde epoch
print(mod)  # Imprime la fecha de la última modificación en segundos desde epoch

print("---------------------------------------------------------")

timestamp = os.path.getmtime("spider.txt")  # Obtiene la fecha de la última modificación del archivo "spider.txt" en segundos desde epoch
# Convierte la fecha de la última modificación de segundos desde epoch a un objeto datetime
fecha_hora = datetime.datetime.fromtimestamp(timestamp)
# Imprime la fecha y hora de la última modificación en un formato legible
print(fecha_hora)
print("---------------------------------------------------------")

ruta = os.path.abspath("spider.txt")  # Obtiene la ruta absoluta del archivo "spider.txt"
# Este código toma el nombre del archivo y lo convierte en una ruta absoluta
print(ruta)  # Imprime la ruta absoluta del archivo
