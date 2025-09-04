"""La función create_python_script crea un nuevo script de Python en el directorio de trabajo actual,
le añade la línea de comentarios declarada por la variable 'comments' y devuelve el tamaño del nuevo archivo.
"""


def create_python_script(filename):
    """
    Crea un nuevo script de Python con un comentario inicial y devuelve su tamaño.

    Args:
        filename (str): El nombre del archivo a crear.

    Returns:
        int: El tamaño del archivo creado (en bytes).
    """
    comments = "# Start of a new Python program"  # Define el comentario inicial para el script
    with open(filename, "w") as f:  # Abre el archivo en modo escritura ("w")
        filesize = f.write(comments)  # Escribe el comentario en el archivo y guarda el número de bytes escritos
    return filesize  # Devuelve el tamaño del archivo


print(create_python_script("program.py"))  # Llama a la función para crear el archivo "program.py" e imprime su tamaño
