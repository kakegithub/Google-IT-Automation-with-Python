
#!/usr/bin/env python3
# Este script contiene una función para reordenar nombres que están
# en el formato "Apellido, Nombre" y devolverlos como "Nombre Apellido".
# Usa expresiones regulares para reconocer el patrón deseado.

import re


def rearrange_name(name):
  # Intentamos encontrar dos grupos separados por una coma y espacio:
  #   1. cualquier combinación de letras, dígitos, subrayados, espacios o puntos
  #   2. otro grupo similar después de la coma
  # La expresión ^...$ fuerza que toda la cadena cumpla con el patrón.
  result = re.search(r"^([\w .]*), ([\w .]*)$", name)

  # Si no hay coincidencia, devolvemos el nombre sin cambios.
  if result is None:
    return name

  # Si se encuentra una coincidencia, construimos la cadena en el orden
  # "Nombre Apellido" usando los grupos capturados 2 y 1.
  return "{} {}".format(result[2], result[1])


# ./rearrange_test.py  -- referencia del archivo de pruebas asociado

