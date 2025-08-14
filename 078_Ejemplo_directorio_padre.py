"""La función directorio_padre devuelve el nombre del directorio que se encuentra justo encima del directorio de trabajo actual. Recuerde que '..' es un alias de ruta de acceso relativa que significa "subir al directorio principal"."""

import os


def parent_directory():
    # Crear una ruta relativa al directorio padre
    relative_parent = os.path.join("..", "")  # Combina ".." con una cadena vacía

    # Devolver la ruta absoluta del directorio padre
    return os.path.abspath(relative_parent)


print(parent_directory())
