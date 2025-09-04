###############################################################################################################


# Calcular la longitud total y promedio de los nombres de animales en una lista
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
total_chars = 0  # Inicializar el contador de caracteres

# Iterar sobre la lista de animales
for animal in animals:
    total_chars += len(animal)  # Sumar la longitud de cada nombre

# Calcular el promedio y mostrar los resultados
average_length = total_chars / len(animals)
print("Total characters: {}, Average length: {}".format(total_chars, average_length))
# Total characters: 22, Average length: 5.5

# Imprimir una lista de ganadores con su posición
winners = ["Ashley", "Dylan", "Reese"]

# Iterar sobre la lista de ganadores usando enumerate para obtener el índice
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))

# 1 - Ashley
# 2 - Dylan
# 3 - Reese

# Crear una lista de strings con el formato "Nombre <email>" a partir de una lista de tuplas (email, Nombre)
def full_emails(people):
    result = []  # Inicializar la lista de resultados
    # Iterar sobre la lista de personas
    for email, name in people:
        result.append("{} <{}>".format(name, email))  # Formatear y agregar a la lista
    return result

# Ejemplo de uso de la función full_emails
print(
    full_emails(
        [("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]
    )
)
# ['Alex Diego <alex@example.com>', 'Shay Brandt <shay@example.com>']

# Crear una lista con los elementos de índice par de una lista dada
def skip_elements(elements):
    # Usar comprensión de listas para seleccionar elementos con índice par
    result = [element for index, element in enumerate(elements) if index % 2 == 0]
    return result

# Ejemplos de uso de la función skip_elements
print(
    skip_elements(["a", "b", "c", "d", "e", "f", "g"])
)  # Should be ['a', 'c', 'e', 'g']
print(
    skip_elements(["Orange", "Pineapple", "Strawberry", "Kiwi", "Peach"])
)  # Should be ['Orange', 'Strawberry', 'Peach']


##########################################################################################################################
