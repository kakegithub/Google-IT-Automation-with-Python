"""
Este script demuestra conceptos básicos de emparejamiento de patrones
con expresiones regulares (regex) en Python usando el módulo `re`.
"""
import re

print("--- 1. Búsqueda de un patrón literal ---")
# re.search() busca un patrón en una cadena y devuelve un objeto "Match" si lo encuentra.
# Si no lo encuentra, devuelve None.

result = re.search(r"aza", "plaza")
print(f"Buscando 'aza' en 'plaza': {result}")

result = re.search(r"aza", "bazaar")
print(f"Buscando 'aza' en 'bazaar': {result}")

result = re.search(r"aza", "maze")
print(f"Buscando 'aza' en 'maze': {result}")  # No lo encontrará, devuelve None

print("\n--- 2. Uso del metacaracter de anclaje de inicio (^) ---")
# El carácter '^' indica que el patrón debe aparecer al principio de la cadena.
result = re.search(r"^x", "xenon")
print(f"Buscando 'x' al inicio de 'xenon': {result}")

result = re.search(r"^p", "xenon")
print(f"Buscando 'p' al inicio de 'xenon': {result}")  # No lo encontrará

print("\n--- 3. Uso del metacaracter comodín (.) ---")
# El carácter '.' (punto) coincide con cualquier carácter individual (excepto salto de línea).
result = re.search(r"p.ng", "penguin")
print(f"Buscando 'p.ng' en 'penguin': {result}")  # '.' coincide con 'e'

result = re.search(r"p.ng", "clapping")
print(f"Buscando 'p.ng' en 'clapping': {result}")  # '.' coincide con 'i'

result = re.search(r"p.ng", "sponge")
print(f"Buscando 'p.ng' en 'sponge': {result}")  # '.' coincide con 'o'

print("\n--- 4. Búsqueda ignorando mayúsculas/minúsculas (re.IGNORECASE) ---")
# El flag re.IGNORECASE hace que la búsqueda no distinga entre mayúsculas y minúsculas.
result = re.search(r"p.ng", "Pangaea", re.IGNORECASE)
# 'p' coincide con 'P' y '.' con 'a'
print(f"Buscando 'p.ng' en 'Pangaea' (ignorando mayúsculas): {result}")
