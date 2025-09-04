"""
La función directorio_padre devuelve el nombre del directorio que se encuentra justo encima del directorio de trabajo actual.
Recuerde que '..' es un alias de ruta de acceso relativa que significa "subir al directorio principal".
"""

import os  # Importa el módulo os para interactuar con el sistema operativo


def parent_directory():
    """
    Devuelve la ruta absoluta del directorio padre del directorio de trabajo actual.

    Returns:
        str: La ruta absoluta del directorio padre.
    """
    # Crear una ruta relativa al directorio padre
    # Combina ".." con una cadena vacía
    relative_parent = os.path.join("..", "")  # Crea una ruta relativa al directorio padre ("..")

    # Devolver la ruta absoluta del directorio padre
    return os.path.abspath(relative_parent)  # Convierte la ruta relativa a una ruta absoluta y la devuelve


print(parent_directory())  # Llama a la función e imprime el resultado
