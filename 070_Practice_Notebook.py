# Abre el archivo "guests.txt" en modo escritura ("w"). Esto creará un nuevo archivo o truncará uno existente.
guests = open("guests.txt", "w")
# Define una lista de nombres de invitados iniciales.
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

# Itera sobre la lista de invitados iniciales.
for i in initial_guests:
    # Escribe cada nombre de invitado en el archivo, seguido de un salto de línea.
    guests.write(i + "\n")

# Cierra el archivo "guests.txt". Es importante cerrar el archivo para liberar los recursos del sistema.
guests.close()

print("-------------------------------------------------------")

# Abre el archivo "guests.txt" en modo lectura ("r") utilizando la instrucción "with".
# La instrucción "with" asegura que el archivo se cierre automáticamente después de su uso.
with open("guests.txt") as guests:
    # Itera sobre cada línea del archivo.
    for line in guests:
        # Imprime cada línea. Cada línea contendrá un nombre de invitado seguido de un salto de línea.
        print(line)


print("-------------------------------------------------------")

# Define una lista de nuevos invitados para agregar al archivo.
new_guests = ["Sam", "Danielle", "Jacob"]

# Abre el archivo "guests.txt" en modo "append" ("a"). Esto agregará los nuevos nombres al final del archivo.
with open("guests.txt", "a") as guests:
    # Itera sobre la lista de nuevos invitados.
    for i in new_guests:
        # Escribe cada nombre de invitado en el archivo, seguido de un salto de línea.
        guests.write(i + "\n")

# Cierra el archivo "guests.txt".
guests.close()

print("-------------------------------------------------------")

# Abre el archivo "guests.txt" en modo lectura ("r") utilizando la instrucción "with".
with open("guests.txt") as guests:
    # Itera sobre cada línea del archivo.
    for line in guests:
        # Imprime cada línea.
        print(line)

print("-------------------------------------------------------")

# Define una lista de invitados que se han retirado.
checked_out = ["Andrea", "Manuel", "Khalid"]
# Inicializa una lista temporal para almacenar los nombres de los invitados que permanecen en el archivo.
temp_list = []

# Abre el archivo "guests.txt" en modo lectura ("r").
with open("guests.txt", "r") as guests:
    # Itera sobre cada línea del archivo.
    for g in guests:
        # Elimina los espacios en blanco al principio y al final de la línea (incluido el salto de línea) y agrega el nombre a la lista temporal.
        temp_list.append(g.strip())

# Abre el archivo "guests.txt" en modo escritura ("w"). Esto truncará el archivo, eliminando todo su contenido anterior.
with open("guests.txt", "w") as guests:
    # Itera sobre la lista temporal de nombres de invitados.
    for name in temp_list:
        # Si el nombre del invitado no está en la lista de invitados que se han retirado,
        if name not in checked_out:
            # Escribe el nombre del invitado en el archivo, seguido de un salto de línea.
            guests.write(name + "\n")

print("-------------------------------------------------------")

# Abre el archivo "guests.txt" en modo lectura ("r") utilizando la instrucción "with".
with open("guests.txt") as guests:
    # Itera sobre cada línea del archivo.
    for line in guests:
        # Imprime cada línea.
        print(line)

print("-------------------------------------------------------")

# Define una lista de invitados para verificar su estado de registro.
guests_to_check = ["Bob", "Andrea"]
# Inicializa una lista para almacenar los nombres de los invitados registrados.
checked_in = []

# Abre el archivo "guests.txt" en modo lectura ("r").
with open("guests.txt", "r") as guests:
    # Itera sobre cada línea del archivo.
    for g in guests:
        # Elimina los espacios en blanco al principio y al final de la línea (incluido el salto de línea) y agrega el nombre a la lista de invitados registrados.
        checked_in.append(g.strip())
    # Itera sobre la lista de invitados para verificar.
    for check in guests_to_check:
        # Si el nombre del invitado está en la lista de invitados registrados,
        if check in checked_in:
            # Imprime un mensaje indicando que el invitado está registrado.
            print("{} is checked in".format(check))
        # De lo contrario,
        else:
            # Imprime un mensaje indicando que el invitado no está registrado.
            print("{} is not checked in".format(check))
