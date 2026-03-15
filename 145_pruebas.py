#!/usr/bin/env python3

# Función para validar un nombre de usuario.
# Verifica que tenga al menos 'minlen' caracteres y sea alfanumérico.
def validate_user(username, minlen):
  # Si minlen es menor que 1, lanzamos un error porque no tiene sentido
  if minlen < 1:
    raise ValueError("minlen must be at least 1")

  # Si la longitud del username es menor que minlen, no es válido
  if len(username) < minlen:
    return False
  # Si no es alfanumérico (solo letras y números), no es válido
  if not username.isalnum():
    return False
  # Si pasa todas las pruebas, es válido
  return True

##############################################
# Ejemplos de uso comentados:
# from validations import validate_user
# validate_user("", -1)  # Esto lanzaría ValueError

##############################################
# from validations import validate_user
# validate_user("", 1)   # Devolvería False (vacío)
# validate_user("myuser", 1)  # Devolvería True (válido)

###############################################
# from validations import validate_user
# validate_user(88, 1)   # Esto causaría TypeError porque username debe ser string

##############################################
# from validations import validate_user
# validate_user([], 1)   # Esto causaría TypeError porque username debe ser string


###################################################
# from validations import validate_user
# validate_user(["name"], 1)
# Esto causaría TypeError porque username debe ser string