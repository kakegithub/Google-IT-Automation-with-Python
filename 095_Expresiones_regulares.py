"""
Este script demuestra el uso de anclas (^ y $) y la construcción de patrones
complejos para validación con expresiones regulares (regex).
"""
import re

print("--- 1. Búsqueda con y sin Anclas ---")
# El patrón "A.*a" busca una 'A', seguida de cualquier carácter (.), cero o más veces (*), y una 'a'.
# Es "greedy" (codicioso), por lo que .* se expande lo máximo posible.
print(f"Buscando 'A.*a' en 'Argentina': {re.search(r'A.*a', 'Argentina')}")
# Coincide con 'Azerbaija'
print(f"Buscando 'A.*a' en 'Azerbaijan': {re.search(r'A.*a', 'Azerbaijan')}")

# Las anclas fuerzan al patrón a coincidir con la cadena completa.
# ^: Ancla de inicio de cadena.
# $: Ancla de fin de cadena.
# El patrón "^A.*a$" busca una cadena que EMPIECE con 'A' y TERMINE con 'a'.
print(f"Buscando '^A.*a$' en 'Australia': {re.search(r'^A.*a$', 'Australia')}")
# No coincide, porque no termina en 'a'
print(
    f"Buscando '^A.*a$' en 'Azerbaijan': {re.search(r'^A.*a$', 'Azerbaijan')}")


print("\n--- 2. Validación de Nombres de Variable ---")
# Este patrón valida si una cadena es un nombre de variable válido en muchos lenguajes.
# ^[a-zA-Z_] : Debe empezar (^) con una letra (mayúscula o minúscula) o un guion bajo.
# [a-zA-Z0-9_]* : Puede ser seguido por cero o más (*) letras, números o guiones bajos.
# $ : Debe terminar ($) ahí, sin más caracteres.
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"


def check_variable(name):
    is_valid = bool(re.search(pattern, name))
    return "Válido" if is_valid else "No válido"


print(
    f"'_this_is_a_valid_variable_name' -> {check_variable('_this_is_a_valid_variable_name')}")
# No válido por el espacio y el apóstrofo
print(
    f"'this isn't a valid variable' -> {check_variable('this isn\'t a valid variable')}")
print(f"'my_variable1' -> {check_variable('my_variable1')}")
# No válido porque empieza con un número
print(f"'2my_variable1' -> {check_variable('2my_variable1')}")
