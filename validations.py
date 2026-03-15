#!/usr/bin/env python3

# Función para validar un nombre de usuario.
# Comprueba:
# - minlen >= 1
# - longitud de username >= minlen
# - username solo contiene caracteres alfanuméricos (letras y números)
def validate_user(username, minlen):
  # Valor mínimo inválido: lanzamos ValueError
  if minlen < 1:
    raise ValueError("minlen must be at least 1")

  # Longitud insuficiente -> usuario no válido
  if len(username) < minlen:
    return False

  # Si hay símbolos especiales o espacios -> usuario no válido
  if not username.isalnum():
    return False

  # Todo bien -> usuario válido
  return True
