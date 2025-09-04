"""
La función nuevo_directorio crea un nuevo directorio dentro del directorio de trabajo actual,
luego crea un nuevo archivo vacío dentro del nuevo directorio, y devuelve la lista de archivos en ese directorio.
"""

import os  # Importa el módulo os para interactuar con el sistema operativo


def new_directory(directory, filename):
    """
    Crea un nuevo directorio, un archivo vacío dentro de él y devuelve la lista de archivos en el directorio.

    Args:
        directory (str): El nombre del directorio a crear.
        filename (str): El nombre del archivo a crear dentro del directorio.

    Returns:
        list: Una lista de los archivos y subdirectorios en el nuevo directorio.
    """
    # Before creating a new directory, check to see if it already exists
    if not os.path.isdir(directory):  # Comprueba si el directorio ya existe
        os.mkdir(directory)  # Crea el directorio si no existe

    # Create the new file inside of the new directory
    os.chdir(directory)  # Cambia el directorio de trabajo al nuevo directorio
    with open(filename, "w") as file:  # Abre el archivo en modo escritura
        pass  # No escribe nada en el archivo (crea un archivo vacío)

    # Return the list of files in the new directory
    os.chdir("..")  # Regresa al directorio anterior
    return os.listdir()  # Devuelve la lista de archivos en el nuevo directorio


# Llama a la función para crear el directorio "PythonPrograms", el archivo "script.py" y luego imprime la lista de archivos en el directorio
print(new_directory("PythonPrograms", "script.py"))
