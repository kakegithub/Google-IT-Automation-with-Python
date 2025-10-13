import csv  # Importa el módulo csv, necesario para trabajar con archivos CSV.

# Abre el archivo 'software.csv' en modo lectura.
# El bloque 'with' asegura que el archivo se cierre automáticamente al finalizar.
with open('software.csv') as software:
    # Crea un objeto 'DictReader' que lee el archivo CSV.
    # Cada fila se convierte en un diccionario, donde las claves son los nombres de las columnas (la primera fila del CSV).
    reader = csv.DictReader(software)

    # Itera sobre cada fila (diccionario) en el archivo CSV.
    for row in reader:
        # Imprime una cadena formateada utilizando los valores de las claves "name" y "users" de la fila actual.
        print("{} has {} users".format(row["name"], row["users"]))
