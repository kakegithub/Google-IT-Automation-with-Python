"""El código leerá los datos del Archivo CSV csv_file.txt e imprimirá la siguiente información para cada fila:
Nombre,Número de teléfono,Función
"""

import csv  # Importa el módulo csv para trabajar con archivos CSV

f = open("csv_file.txt")  # Abre el archivo "csv_file.txt" en modo lectura
csv_f = csv.reader(f)  # Crea un objeto lector CSV para leer el archivo abierto
for row in csv_f:  # Itera sobre cada fila del archivo CSV
    name, phone, role = row  # Desempaqueta los valores de la fila en las variables name, phone y role
    print(
        "Name: {}, Phone: {}, Role: {}".format(name, phone, role)
    )  # Imprime la información formateada para cada fila
f.close()  # Cierra el archivo para liberar los recursos
