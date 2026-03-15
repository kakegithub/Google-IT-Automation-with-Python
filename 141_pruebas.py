import unittest


# Este archivo contiene pruebas unitarias básicas para métodos de cadenas
# utilizando el framework unittest de Python.
class TestStringMethods(unittest.TestCase):

    # Comprueba que upper() convierte a mayúsculas correctamente
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    # Verifica comportamiento de isupper():
    # - debe ser True para strings completamente en mayúsculas
    # - debe ser False si hay alguna letra minúscula
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    # Asegura que split() divida la cadena en palabras cuando no se da separador
    # y que lance un TypeError si se pasa un separador no string.
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # comprobamos que split falla cuando el separador no es una cadena
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    # Ejecuta las pruebas al invocar el script directamente
    unittest.main()
