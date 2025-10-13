"""
Este script demuestra cómo escapar metacaracteres y el uso de secuencias
de caracteres especiales como \w en expresiones regulares (regex).
"""
import re

print("--- 1. Escapando Metacaracteres ---")
# El punto '.' es un metacaracter que coincide con CUALQUIER carácter.
# Por lo tanto, '.com' coincide con 'lcom' en 'welcome'.
print(
    f"Buscando '.com' (comodín) en 'welcome': {re.search(r'.com', 'welcome')}")

# Para buscar un punto literal, debemos "escaparlo" con una barra invertida '\'.
# El patrón r'\.com' no encuentra nada en 'welcome' porque no hay un punto literal.
print(
    f"Buscando '\.com' (literal) en 'welcome': {re.search(r'\.com', 'welcome')}")

# Aquí sí encuentra una coincidencia porque la cadena contiene '.com'.
print(
    f"Buscando '\.com' (literal) en 'mydomain.com': {re.search(r'\.com', 'mydomain.com')}")


print("\n--- 2. Secuencias Especiales de Caracteres ---")
# \w es una secuencia especial que coincide con cualquier "carácter de palabra":
# letras (a-z, A-Z), números (0-9) y el guion bajo (_).
# El cuantificador * significa "cero o más veces".
# \w* coincide con la secuencia más larga posible de caracteres de palabra.
print(
    f"Buscando '\w*' en 'This is an example': {re.search(r'\w*', 'This is an example')}")

# Como el guion bajo también es un carácter de palabra, \w* coincide con toda la cadena.
print(
    f"Buscando '\w*' en 'And_this_is_another': {re.search(r'\w*', 'And_this_is_another')}")
