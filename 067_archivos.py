#  Manejo de archivos en Python
file = open("spider.txt")
# Lee la primera línea del archivo
print(file.readline())
# Lee la segunda línea del archivo
print(file.readline())
# Lee desde la posición actual hasta el final
print(file.read())
# Cierra el archivo
file.close()

# También se puede usar la instrucción with para manejar archivos,
# que cierra automáticamente el archivo al finalizar el bloque
with open("spider.txt") as file:
    print(file.readline())
