"""
Este script demuestra el uso de los cuantificadores de repetición básicos
en expresiones regulares (regex) con el módulo `re` de Python:
- * (cero o más veces)
- + (una o más veces)
- ? (cero o una vez)
"""
import re

print("--- 1. Cuantificador * (cero o más veces) ---")
# El patrón "Py.*n" busca 'Py', seguido de CUALQUIER carácter (.), CERO o MÁS veces (*).
# Es "greedy" (codicioso), por lo que intenta abarcar el máximo texto posible.
print(f"Buscando 'Py.*n' en 'Pygmalion': {re.search(r'Py.*n', 'Pygmalion')}")
# Coincide hasta la última 'n'
print(
    f"Buscando 'Py.*n' en 'Python Programming': {re.search(r'Py.*n', 'Python Programming')}")

# El patrón "Py[a-z]*n" es más específico. Busca 'Py', seguido de letras minúsculas, CERO o MÁS veces.
# Se detiene en el espacio
print(
    f"Buscando 'Py[a-z]*n' en 'Python Programming': {re.search(r'Py[a-z]*n', 'Python Programming')}")
# Coincide porque '*' permite cero letras entre 'Py' y 'n'
print(f"Buscando 'Py[a-z]*n' en 'Pyn': {re.search(r'Py[a-z]*n', 'Pyn')}")


print("\n--- 2. Cuantificador + (una o más veces) ---")
# El patrón "o+l+" busca UNA o MÁS 'o' seguidas de UNA o MÁS 'l'.
# Coincide con 'ol'
print(f"Buscando 'o+l+' en 'goldfish': {re.search(r'o+l+', 'goldfish')}")
# Coincide con 'ooll'
print(f"Buscando 'o+l+' en 'woolly': {re.search(r'o+l+', 'woolly')}")
# No coincide porque no hay 'l' después de la 'o'
print(f"Buscando 'o+l+' en 'boil': {re.search(r'o+l+', 'boil')}")


print("\n--- 3. Cuantificador ? (cero o una vez / opcional) ---")
# El patrón "p?each" busca una 'p' OPCIONAL (cero o una vez) seguida de 'each'.
# Coincide con 'each'
print(
    f"Buscando 'p?each' en 'To each their own': {re.search(r'p?each', 'To each their own')}")
# Coincide con 'peach'
print(
    f"Buscando 'p?each' en 'I like peaches': {re.search(r'p?each', 'I like peaches')}")
