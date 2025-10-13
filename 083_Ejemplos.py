import os
import csv


def create_file(filename):
    """
    Crea un archivo CSV con datos de flores. Si el archivo ya existe,
    lo sobrescribe.

    Args:
        filename (str): El nombre del archivo a crear (ej. "flowers.csv").
    """
    # Se abre el archivo en modo escritura ('w').
    # 'newline=""' es importante al escribir CSVs para evitar filas en blanco adicionales.
    with open(filename, "w", newline='') as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")


def contents_of_file(filename):
    """
    Lee un archivo CSV de flores y devuelve una cadena formateada con su contenido.

    Args:
        filename (str): El nombre del archivo CSV a leer.

    Returns:
        str: Una cadena de texto con la información de cada flor, línea por línea.
    """
    return_string = ""

    # Llama a la función para asegurarse de que el archivo exista y tenga contenido.
    create_file(filename)

    # Abre el archivo en modo lectura. El bloque 'with' asegura que se cierre automáticamente.
    with open(filename) as file:
        # csv.DictReader interpreta cada fila como un diccionario, usando la
        # primera fila como las claves (headers: "name", "color", "type").
        reader = csv.DictReader(file)

        # Itera sobre cada fila (que es un diccionario) en el archivo.
        for row in reader:
            # Formatea la cadena usando los valores del diccionario de la fila actual
            # y la añade a la cadena de resultado.
            return_string += "a {} {} is {}\n".format(
                row["color"], row["name"], row["type"])
    return return_string


# Llama a la función principal e imprime el resultado final.
print(contents_of_file("flowers.csv"))
