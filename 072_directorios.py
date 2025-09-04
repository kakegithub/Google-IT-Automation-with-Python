import os  # Importa el módulo os para interactuar con el sistema operativo

print(os.getcwd())
# This code snippet returns the current working directory.
# Imprime el directorio de trabajo actual.

os.mkdir("new_dir")
# The os.mkdir("new_dir") function creates a new directory called new_dir
# in the current working directory.
# Crea un nuevo directorio llamado "new_dir" en el directorio de trabajo actual.

os.chdir("new_dir")
# Cambia el directorio de trabajo actual a "new_dir".
print(os.getcwd())
# This code snippet changes the current working directory to new_dir.
# The second line prints the current working directory.
# Imprime el directorio de trabajo actual (que ahora es "new_dir").

os.mkdir("newer_dir")
# Crea un nuevo directorio llamado "newer_dir" dentro del directorio actual ("new_dir").
os.rmdir("newer_dir")
# This code snippet creates a new directory called newer_dir.
# The second line deletes the newer_dir directory.
# Elimina el directorio "newer_dir".

print(os.listdir("website"))
# This code snippet returns a list of all the files and
# sub-directories in the website directory.
# Imprime una lista de todos los archivos y subdirectorios en el directorio "website".

dir = "website"  # Define la variable "dir" con el valor "website"
for name in os.listdir(dir):  # Itera sobre cada archivo o directorio dentro de "website"
    fullname = os.path.join(dir, name)  # Construye la ruta completa al archivo o directorio
    if os.path.isdir(fullname):  # Comprueba si la ruta completa es un directorio
        print("{} is a directory".format(fullname))  # Imprime que es un directorio
    else:  # Si no es un directorio (es un archivo)
        print("{} is a file".format(fullname))  # Imprime que es un archivo
