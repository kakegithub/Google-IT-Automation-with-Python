with open("spider.txt") as file:
    # Itera a través de cada línea del archivo
    for line in file:
        # Imprime la línea actual en mayúsculas
        print(line.upper())  # Imprime la línea en mayúsculas (incluyendo el salto de línea al final)

print("-----")  # Imprime una línea separadora

with open("spider.txt") as file:
    # Itera a través de cada línea del archivo
    for line in file:
        # Imprime la línea actual en mayúsculas, eliminando el salto de línea al final
        print(line.strip().upper())  # Elimina los espacios en blanco al principio y al final de la línea, la convierte a mayúsculas y la imprime

print("-----")  # Imprime una línea separadora

with open("spider.txt") as file:
    # Lee todas las líneas del archivo y las almacena en una lista
    lines = file.readlines()
    # El archivo se cierra automáticamente al salir del bloque "with", por lo que no es necesario cerrarlo explícitamente
    # file.close()  # Cierra el archivo (innecesario con la instrucción "with")
    lines.sort()  # Ordena las líneas alfabéticamente
    print(lines)  # Imprime la lista de líneas ordenadas

print("-----")  # Imprime una línea separadora
