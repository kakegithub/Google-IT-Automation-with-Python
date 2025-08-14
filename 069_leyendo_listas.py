"""El argumento mode es opcional, y especifica el modo en el que se abre el archivo. Si se omite, por defecto es "r" y eso significa abrir para lectura en modo texto. Los modos comunes incluyen:

"r" abrir para lectura (por defecto)

"w" abrir para escribir, truncando el archivo primero

"x" abrir para creación exclusiva, fallando si el archivo ya existe

"a" abierto para escritura, añadiendo el final del archivo si existe

"+" abierto tanto para lectura como para escritura
"""

file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)


with open("novel.txt", "w") as file:
    file.write(
        "Once upon a time, there was a brave knight who fought dragons and saved kingdoms."
    )

with open("declaration.txt", "rt") as textfile:
    for line in textfile:
        print(line)

f = open("declaration.txt", "w")

f = open("workfile", "w", encoding="utf-8")
