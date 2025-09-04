# Operadores de igualdad (==) y desigualdad (!=) con cadenas en Python

# El operador == verifica si dos cadenas son iguales.
print("a string" == "a string")  # True: las cadenas son idénticas

# Comparación entre tipos distintos: str vs int.
# "4 + 5" es una cadena y 4 + 5 es el entero 9. La igualdad entre tipos distintos es False.
print("4 + 5" == 4 + 5)  # False

# El operador != verifica si dos valores NO son iguales.
print("rabbit" != "frog")  # True: las cadenas son diferentes

# Comparación de una variable cadena con otra cadena literal.
event_city = "Shanghai"
print(event_city != "Shanghai")  # False: ambas cadenas son iguales, por lo que no son distintas

# Comparar cadena con entero devuelve False (tipos distintos y valores no equivalentes).
print("three" == 3)  # False
