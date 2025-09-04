# Manejo de archivos en Python
file = open("spider.txt")  # Abre el archivo "spider.txt" en modo lectura

# Lee la primera línea del archivo
print(file.readline())  # Imprime la primera línea del archivo

# Lee la segunda línea del archivo
print(file.readline())  # Imprime la segunda línea del archivo

# Lee desde la posición actual hasta el final
print(file.read())  # Imprime el resto del archivo desde la posición actual

# Cierra el archivo
file.close()  # Cierra el archivo para liberar los recursos

# También se puede usar la instrucción with para manejar archivos,
# que cierra automáticamente el archivo al finalizar el bloque
with open("spider.txt") as file:  # Abre el archivo "spider.txt" en modo lectura utilizando la instrucción with
    print(file.readline())  # Imprime la primera línea del archivo
# El archivo se cierra automáticamente al salir del bloque with
