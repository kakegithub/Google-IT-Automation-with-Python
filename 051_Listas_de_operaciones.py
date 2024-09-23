# Convert a list to a tuple
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)

print(my_tuple)  # Outputs: (1, 2, 3, 4)

# Remember that although parentheses are often used to define a tuple,
# they're not always necessary. The following syntax is also valid:

my_tuple = 1, 2, 3, 4
print(my_tuple)  # Outputs: (1, 2, 3, 4)


#########################################################################################################

# Tuplas con objetos mutables

# A tuple with a list as an element
my_tuple = (1, 2, ["a", "b", "c"])

# You can't change the tuple itself
# my_tuple[0] = 3  # This would raise a TypeError

# But you can modify the mutable elements within the tuple
my_tuple[2][0] = "x"
print(my_tuple)  # Outputs: (1, 2, ['x', 'b', 'c'])


################################################################################################################

# Devolución de múltiples valores desde funciones


def calculate_numbers(a, b):
    return a + b, a - b, a * b, a / b


result = calculate_numbers(10, 2)
print(result)  # Outputs: (12, 8, 20, 5.0)


################################################################################################################


def calculate_numbers(a, b):
    return a + b, a - b, a * b, a / b


add_result, sub_result, mul_result, div_result = calculate_numbers(10, 2)
print(add_result)  # Outputs: 12
print(sub_result)  # Outputs: 8


###################################################################################################################

# Comprensión de listas

# [expresión para variable en secuencia] - Crea una nueva lista basada en la secuencia dada. Cada elemento de la nueva lista es el resultado de la expresión dada.

my_list = [x * 2 for x in range(1, 11)]

# [expresión para variable en secuencia si condición ] - Crea una nueva lista basada en una secuencia especificada. Cada elemento es el resultado de la expresión dada; sólo se añaden elementos si la condición especificada es verdadera.

my_list = [x for x in range(1, 101) if x % 10 == 0]


#########################################################################################################################

# El operador tuple() se utiliza para convertir un iterable (como una lista, una cadena o un conjunto) en una tupla.

# Convert a list to a tuple
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)

print(my_tuple)  # Outputs: (1, 2, 3, 4)

# Remember that although parentheses are often used to define a tuple,
# they're not always necessary. The following syntax is also valid:

my_tuple = 1, 2, 3, 4
print(my_tuple)  # Outputs: (1, 2, 3, 4)

#############################################################################################################################

# Tuplas con objetos mutables

# A tuple with a list as an element
my_tuple = (1, 2, ["a", "b", "c"])

# You can't change the tuple itself
# my_tuple[0] = 3  # This would raise a TypeError

# But you can modify the mutable elements within the tuple
my_tuple[2][0] = "x"
print(my_tuple)  # Outputs: (1, 2, ['x', 'b', 'c'])

##############################################################################################################################


# Devolución de múltiples valores desde funciones


def calculate_numbers(a, b):
    return a + b, a - b, a * b, a / b


result = calculate_numbers(10, 2)
print(result)  # Outputs: (12, 8, 20, 5.0)

##############################################################################################################################


def calculate_numbers(a, b):
    return a + b, a - b, a * b, a / b


add_result, sub_result, mul_result, div_result = calculate_numbers(10, 2)
print(add_result)  # Outputs: 12
print(sub_result)  # Outputs: 8


#################################################################################################################################
