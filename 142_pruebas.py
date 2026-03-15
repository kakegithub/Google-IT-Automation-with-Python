import unittest

# Clase que representa una biblioteca simple con una colección de títulos
class Library:
    def __init__(self):
        # Usamos una lista para almacenar los títulos de los libros
        self.collection = []

    def add_book(self, book_title):
        # Agrega un título a la colección
        self.collection.append(book_title)

    def has_book(self, book_title):
        # Devuelve True si el título está en la colección
        return book_title in self.collection


# Pruebas unitarias para el sistema de biblioteca
class TestLibrary(unittest.TestCase):

    def test_adding_book_to_library(self):
        # Preparación (Arrange): crear biblioteca y libro nuevo
        library = Library()
        new_book = "Python Design Patterns"

        # Acción (Act): añadir el libro
        library.add_book(new_book)

        # Comprobación (Assert): la biblioteca debe contener el libro añadido
        self.assertTrue(library.has_book(new_book))


# Ejecutar la prueba cuando se ejecuta este script directamente
library_test_output = unittest.TextTestRunner().run(
    unittest.TestLoader().loadTestsFromTestCase(TestLibrary)
)
print(library_test_output)
