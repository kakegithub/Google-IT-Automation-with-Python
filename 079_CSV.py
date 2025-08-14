"""El código leerá los datos del Archivo CSV csv_file.txt e imprimirá la siguiente información para cada fila:Nombre,Número de teléfono,Función"""

import csv
f = open("csv_file.txt")
cvs_f = cvs.reader(f)
    for row in cvs_f:
        name, phone, role = row
        print("name:{}, phone:{}, role:{}".formsat(name, phone, role))
f.close()
"""El código leerá los datos del Archivo CSV csv_file.txt e imprimirá la siguiente información para cada fila: Nombre, Número de teléfono, Función"""
