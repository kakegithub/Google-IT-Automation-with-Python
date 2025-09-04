"""El argumento mode es opcional, y especifica el modo en el que se abre el archivo. Si se omite, por defecto es "r" y eso significa abrir para lectura en modo texto. Los modos comunes incluyen:

"r" abrir para lectura (por defecto)

"w" abrir para escribir, truncando el archivo primero

"x" abrir para creación exclusiva, fallando si el archivo ya existe

"a" abierto para escritura, añadiendo el final del archivo si existe

"+" abierto tanto para lectura como para escritura
"""

# Abre el archivo "spider.txt" en modo lectura
file = open("spider.txt")
# Lee todas las líneas del archivo y las guarda en una lista llamada "lines"
lines = file.readlines()
# Cierra el archivo para liberar los recursos
file.close()
# Ordena la lista de líneas alfabéticamente
lines.sort()
# Imprime la lista ordenada de líneas
print(lines)


# Abre el archivo "novel.txt" en modo escritura ("w"), lo que truncará el archivo si ya existe o lo creará si no existe
with open("novel.txt", "w") as file:
    # Escribe una cadena en el archivo
    file.write(
        "Once upon a time, there was a brave knight who fought dragons and saved kingdoms."
    )

# Abre el archivo "declaration.txt" en modo lectura de texto ("rt")
with open("declaration.txt", "rt") as textfile:
    # Itera sobre cada línea del archivo
    for line in textfile:
        # Imprime cada línea
        print(line)

# Abre el archivo "declaration.txt" en modo escritura ("w")
f = open("declaration.txt", "w")

# Abre el archivo "workfile" en modo escritura ("w") con codificación UTF-8
f = open("workfile", "w", encoding="utf-8")
