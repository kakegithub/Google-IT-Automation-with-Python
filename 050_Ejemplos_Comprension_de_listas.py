# Puedes crear una lista a partir de un iterable utilizando un bucle for, que es una forma útil de iterar sobre un iterable:

""" new_list = []
for thing in list_of_things:
    new_list.append[do_something(thing)]

 """

#########################################################################################################################################

#  Una comprensión de lista permite crear una nueva lista a partir de un iterable en una sola línea. Esta línea consigue el mismo resultado que el bucle for anterior, pero de una forma más concisa:

# new_list = [do_something(thing) for thing in list_of_things]

#############################################################################################################################################


# Crear una lista de tuplas, donde cada tupla contiene los números 1, 2 y 3.
numbers = [(1, 2, 3) for _ in range(5)]
print(numbers)
# Resultado: [(1, 2, 3), (1, 2, 3), (1, 2, 3), (1, 2, 3), (1, 2, 3)]

### Comprensión de lista simple
print("List comprehension result:")

# La siguiente comprensión de lista compacta varias líneas de código en una sola línea:
print([x * 2 for x in range(1, 11)])
# Resultado: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

### Forma larga del bucle for
print("Long form code result:")

# La comprensión de lista anterior logra el mismo resultado que la versión de código de forma larga que se muestra a continuación:
my_list = []
for x in range(1, 11):
    my_list.append(x * 2)
print(my_list)
# Resultado: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Comprensión de lista con Sentencia condicional
print("List comprehension result:")
print([x for x in range(1, 101) if x % 10 == 0])
# Resultado: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# La comprensión de lista anterior logra el mismo resultado que la versión de código de forma larga:
print("Long form code result:")
my_list = []
for x in range(1, 101):
    if x % 10 == 0:
        my_list.append(x)
print(my_list)
# Resultado: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


def squares(start, end):
    # Devuelve una lista con los cuadrados de los números en el rango [start, end]
    return [n**2 for n in range(start, end + 1)]


print(squares(2, 3))  # Debería imprimir [4, 9]
print(squares(1, 5))  # Debería imprimir [1, 4, 9, 16, 25]
print(squares(0, 10))  # Debería imprimir [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#######################################################################################################################################################
