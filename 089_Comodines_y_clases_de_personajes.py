"""
Este script demuestra el uso de clases de caracteres, comodines y alternancia
en expresiones regulares (regex) con el módulo `re` de Python.
"""
import re

print("--- 1. Clases de Caracteres `[]` ---")
# [Pp] coincide con 'P' mayúscula o 'p' minúscula. Útil para búsquedas case-insensitive selectivas.
print(f"Buscando '[Pp]ython' en 'Python': {re.search(r'[Pp]ython', 'Python')}")

# [a-z] coincide con cualquier letra minúscula.
print(
    f"Buscando '[a-z]way' en 'The end of the highway': {re.search(r'[a-z]way', 'The end of the highway')}")
print(
    f"Buscando '[a-z]way' en 'What a way to go': {re.search(r'[a-z]way', 'What a way to go')}")

# [a-zA-Z0-9] coincide con cualquier letra (mayúscula o minúscula) o cualquier dígito.
print(
    f"Buscando 'cloud[a-zA-Z0-9]' en 'cloudy': {re.search(r'cloud[a-zA-Z0-9]', 'cloudy')}")
print(
    f"Buscando 'cloud[a-zA-Z0-9]' en 'cloud9': {re.search(r'cloud[a-zA-Z0-9]', 'cloud9')}")


print("\n--- 2. Clases de Caracteres Negadas `[^]` ---")
# [^...] coincide con cualquier carácter que NO esté en el conjunto.
# [^a-zA-Z] coincide con cualquier cosa que no sea una letra. En este caso, el primer espacio.
print(
    f"Buscando '[^a-zA-Z]' en 'This is a sentence with spaces.': {re.search(r'[^a-zA-Z]', 'This is a sentence with spaces.')}")

# [^a-zA-Z ] coincide con cualquier cosa que no sea una letra NI un espacio. En este caso, el punto.
print(
    f"Buscando '[^a-zA-Z ]' en 'This is a sentence with spaces.': {re.search(r'[^a-zA-Z ]', 'This is a sentence with spaces.')}")


print("\n--- 3. Alternancia (OR) con `|` ---")
# El operador `|` (pipe) permite buscar una subcadena U otra.
print(
    f"Buscando 'cat|dog' en 'I like cats.': {re.search(r'cat|dog', 'I like cats.')}")
print(
    f"Buscando 'cat|dog' en 'I love dogs!': {re.search(r'cat|dog', 'I love dogs!')}")


print("\n--- 4. `re.search` vs `re.findall` ---")
# re.search() se detiene en la PRIMERA coincidencia que encuentra.
print(
    f"Con re.search, buscando 'cat|dog' en 'I like both dogs and cats.': {re.search(r'cat|dog', 'I like both dogs and cats.')}")

# re.findall() encuentra TODAS las coincidencias no superpuestas y las devuelve como una lista.
print(
    f"Con re.findall, buscando 'cat|dog' en 'I like both dogs and cats.': {re.findall(r'cat|dog', 'I like both dogs and cats.')}")
