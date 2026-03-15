#!/usr/bin/env python3

import unittest

from validations import validate_user


# Clase de pruebas para la función validate_user
class TestValidateUser(unittest.TestCase):
  # Caso de prueba: usuario válido (longitud correcta y caracteres válidos)
  def test_valid(self):
    self.assertEqual(validate_user("validuser", 3), True)

  # Caso de prueba: nombre demasiado corto en comparación con minlen
  def test_too_short(self):
    self.assertEqual(validate_user("inv", 5), False)

  # Caso de prueba: caracteres no válidos (el guion bajo no está permitido)
  def test_invalid_characters(self):
    self.assertEqual(validate_user("invalid_user", 1), False)

  # Caso de prueba: minlen inválido (negativo) -> debe lanzar ValueError
  def test_invalid_minlen(self):
    self.assertRaises(ValueError, validate_user, "user", -1)


# Ejecuta el conjunto de pruebas
unittest.main()
