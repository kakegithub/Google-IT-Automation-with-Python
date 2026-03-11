#!/usr/bin/env python3

# Este archivo contiene una función de utilidad para reordenar nombres
# y una prueba unitaria que valida su comportamiento.

from rearrange import rearrange_name
import unittest
import re


# La siguiente función redefine `rearrange_name` para fines de ejecución
# directa desde este script; en un uso normal se importaría desde el
# módulo `rearrange` (como se hace más arriba).
def rearrange_name(name):
    """Toma un nombre en formato "Apellido, Nombre" y devuelve
    "Nombre Apellido".

    Args:
        name (str): nombre completo separado por coma.

    Returns:
        str: nombre reordenado sin coma.
    """
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    # `result[1]` contiene el apellido, `result[2]` el nombre.
    return "{} {}".format(result[2], result[1])


#!/usr/bin/env python3


class TestRearrange(unittest.TestCase):
    """Conjunto de pruebas unitarias para la función `rearrange_name`."""

    def test_basic(self):
        # Caso básico: apellido y nombre separados por coma y espacio.
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)


# Ejecutar las pruebas cuando se ejecuta el script directamente.
if __name__ == "__main__":
    unittest.main()

# Comentarios de uso: hacer ejecutable y lanzar desde la línea
# chmod +x rearrange_test.py
# ./rearrange_test.py


""" chmod + x rearrange_test.py
./rearrange_test.py
 """