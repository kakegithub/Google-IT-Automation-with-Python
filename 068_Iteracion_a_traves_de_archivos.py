with open("spider.txt") as file:
    # Itera a través de cada línea del archivo
    for line in file:
        # Imprime la línea actual
        print(line.upper())  # Elimina el salto de línea al final de cada línea

print("-----")

with open("spider.txt") as file:
    # Itera a través de cada línea del archivo
    for line in file:
        # Imprime la línea actual sin el salto de línea al final
        print(line.strip().upper())  # Elimina el salto de línea al final de cada línea

print("-----")

with open("spider.txt") as file:
    lines = file.readlines()
    # Lee todas las líneas del archivo y las almacena en una lista
    file.close()  # Cierra el archivo
    lines.sort()  # Ordena las líneas alfabéticamente
    print(lines)  # Imprime la lista de líneas ordenadas
