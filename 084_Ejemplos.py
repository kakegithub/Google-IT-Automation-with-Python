import os
import csv

# Create a file with data in it


def create_file(filename):
    # Se abre en modo escritura ('w') y con newline='' para evitar líneas en blanco extra.
    with open(filename, "w", newline='') as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")


def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Abre el archivo en modo lectura. El bloque 'with' asegura que se cierre automáticamente.
    with open(filename) as file:
        # Lee las filas del archivo. csv.reader trata cada fila como una lista de strings.
        rows = csv.reader(file)

        # Saltamos la primera fila, que es la cabecera (header), para no procesarla como datos.
        next(rows)

        # Procesa cada fila (que es una lista) en el archivo.
        for row in rows:
            # Desempaquetamos la lista 'row' en variables individuales.
            # Por ejemplo: name="carnation", color="pink", type="annual"
            name, color, type = row

            # Formatea la cadena de retorno usando las variables desempaquetadas.
            # Nota: El orden en el format() es importante para que coincida con la frase.
            return_string += "a {} {} is {}\n".format(color, name, type)

    return return_string


# Llama a la función e imprime el resultado.
print(contents_of_file("flowers.csv"))
