"""
Este script demuestra dos métodos para extraer información de una cadena de texto:
1. Usando métodos de cadena estándar como index() y slicing (frágil).
2. Usando expresiones regulares (más robusto y flexible).

El objetivo es extraer el número de proceso (PID) de una línea de log.
"""

import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

print("--- Método 1: Usando index() y slicing (poco flexible) ---")
# Este método busca la posición del '[' y luego extrae un número fijo de caracteres.
# Es frágil: si el PID tuviera un número diferente de dígitos, fallaría.
try:
    index = log.index("[")
    # Suponemos que el PID siempre tiene 5 dígitos, lo cual no es una buena práctica.
    print(f"PID extraído manualmente: {log[index+1:index+6]}")
except ValueError:
    print("No se encontró el carácter '[' en el log.")


print("\n--- Método 2: Usando Expresiones Regulares (recomendado) ---")
# Define el patrón de la expresión regular.
# r"..." indica una cadena "raw" para que los backslashes no se interpreten como secuencias de escape.
# \[ y \] : Coinciden con los corchetes literales. Se escapan porque tienen un significado especial en regex.
# (\d+) : Es un grupo de captura (indicado por los paréntesis).
#   \d  : Coincide con cualquier dígito (0-9).
#   +   : Coincide con una o más ocurrencias del elemento anterior (en este caso, uno o más dígitos).
regex = r"\[(\d+)\]"

# re.search() busca el patrón en la cadena y devuelve un objeto "match" si lo encuentra.
result = re.search(regex, log)

# El objeto "match" nos permite acceder a las partes capturadas.
# result[0] contendría la coincidencia completa (ej: "[12345]").
# result[1] contiene solo lo que capturó el primer grupo de paréntesis (ej: "12345").
if result:
    print(f"PID extraído con regex: {result[1]}")
else:
    print("No se encontró un PID con el formato esperado en el log.")
