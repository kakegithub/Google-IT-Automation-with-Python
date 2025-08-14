"""El código leerá los datos del Archivo CSV csv_file.txt e imprimirá la siguiente información para cada fila:Nombre,Número de teléfono,Función"""

import csv
f = open("csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, role = row
print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
f.close()
