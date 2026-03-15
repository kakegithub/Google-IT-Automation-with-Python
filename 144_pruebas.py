#!/usr/bin/env python3

# Función que cuenta la frecuencia de cada carácter en un archivo dado.
def character_frequency(filename):
  """Cuenta la frecuencia de cada carácter en el archivo dado."""
  # Primero intentamos abrir el archivo
  try:
    f = open(filename)
  except OSError:
    # Si hay un error al abrir (por ejemplo, archivo no encontrado), devolvemos None
    return None

  # Ahora procesamos el archivo línea por línea
  characters = {}  # Diccionario para almacenar las frecuencias
  for line in f:
    for char in line:
      # Usamos get para incrementar el contador, inicializando en 0 si no existe
      characters[char] = characters.get(char, 0) + 1
  f.close()  # Cerramos el archivo después de procesarlo
  return characters
