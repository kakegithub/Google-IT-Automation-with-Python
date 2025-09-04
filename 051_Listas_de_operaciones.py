# --- Conversión de lista a tupla ---
# El operador tuple() se utiliza para convertir un iterable (como una lista, una cadena o un conjunto) en una tupla.

# Convertir una lista a una tupla
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)

print(my_tuple)  # Imprime: (1, 2, 3, 4)

# Aunque los paréntesis se utilizan a menudo para definir una tupla, no siempre son necesarios.
# La siguiente sintaxis también es válida:

my_tuple = 1, 2, 3, 4
print(my_tuple)  # Imprime: (1, 2, 3, 4)

# --- Tuplas con objetos mutables ---

# Una tupla con una lista como elemento
my_tuple = (1, 2, ["a", "b", "c"])

# No se puede cambiar la tupla en sí
# my_tuple[0] = 3  # Esto generaría un TypeError

# Pero se pueden modificar los elementos mutables dentro de la tupla
my_tuple[2][0] = "x"
print(my_tuple)  # Imprime: (1, 2, ['x', 'b', 'c'])

# --- Devolución de múltiples valores desde funciones ---

# Ejemplo de función que devuelve múltiples valores como una tupla
def calculate_numbers(a, b):
    """
    Calcula la suma, resta, multiplicación y división de dos números.

    Args:
        a: El primer número.
        b: El segundo número.

    Returns:
        Una tupla que contiene la suma, resta, multiplicación y división de a y b.
    """
    return a + b, a - b, a * b, a / b


result = calculate_numbers(10, 2)
print(result)  # Imprime: (12, 8, 20, 5.0)

# Desempaquetado de los valores devueltos por la función
add_result, sub_result, mul_result, div_result = calculate_numbers(10, 2)
print(add_result)  # Imprime: 12
print(sub_result)  # Imprime: 8

# --- Comprensión de listas ---

# [expresión para variable en secuencia] - Crea una nueva lista basada en la secuencia dada.
# Cada elemento de la nueva lista es el resultado de la expresión dada.

my_list = [x * 2 for x in range(1, 11)]
print(my_list)  # Imprime: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# [expresión para variable en secuencia si condición ] - Crea una nueva lista basada en una secuencia especificada.
# Cada elemento es el resultado de la expresión dada; sólo se añaden elementos si la condición especificada es verdadera.

my_list = [x for x in range(1, 101) if x % 10 == 0]
print(my_list)  # Imprime: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
