# Notebook de práctica - pruebas unitarias y casos límite
# En este archivo practicamos la escritura de tests con el marco `unittest`
# y la identificación de casos borde. También usamos expresiones regulares
# para compilar letras específicas de un texto.

import unittest
import re

# texto de ejemplo para probar la función directamente
my_txt = "An investment in knowledge pays the best interest."


def LetterCompiler(txt):
    # Busca, usando una expresión regular, cualquier letra de la a a la c
    # seguida de cualquier carácter (el punto en el patrón). Devuelve una lista
    # con las letras encontradas.
    result = re.findall(r'([a-c]).', txt)
    return result


# demostración rápida de la función con el texto de muestra
print(LetterCompiler(my_txt))

#############################################################################


class TestCompiler(unittest.TestCase):

    def test_basic(self):
        # Caso de prueba sencillo que verifica el comportamiento esperado
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)
#############################################################################


# Llamamos a unittest.main para ejecutar las pruebas si se ejecuta el script
unittest.main()

# En notebooks se suele pasar argv para que no intente interpretar los argumentos
unittest.main(argv=['first-arg-is-ignored'], exit=False)


class TestCompiler2(unittest.TestCase):

    def test_two(self):
        # Otro caso con un conjunto de letras consecutivas para evaluar el patrón
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

# AQUÍ SE PODRÍAN AÑADIR MÁS CASOS PARA CUBRIR ESCENARIOS LÍMITE


unittest.main(argv=['first-arg-is-ignored'], exit=False)

##############################################################################