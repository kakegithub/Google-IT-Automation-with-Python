"""La función create_python_script crea un nuevo script de Python en el directorio de trabajo actual, le añade la línea de comentarios declarada por la variable 'comments' y devuelve el tamaño del nuevo archivo."""


def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w") as f:
        filesize = f.write(comments)
    return filesize


print(create_python_script("program.py"))
