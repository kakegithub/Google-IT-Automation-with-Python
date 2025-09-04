# Create a directory and move a file from one directory to another
# using low-level OS functions.

import os  # Importa el módulo os para interactuar con el sistema operativo

# Check to see if a directory named "test1" exists under the current
# directory. If not, create it:
dest_dir = os.path.join(
    os.getcwd(), "test1"
)  # Construye la ruta completa al directorio "test1"
if not os.path.exists(
    dest_dir
):  # Comprueba si el directorio "test1" existe
    os.mkdir(
        dest_dir
    )  # Crea el directorio "test1" si no existe

# Construct source and destination paths:
src_file = os.path.join(
    os.getcwd(), "sample_data", "README.md"
)  # Construye la ruta completa al archivo de origen "README.md"
dest_file = os.path.join(
    os.getcwd(), "test1", "README.md"
)  # Construye la ruta completa al archivo de destino "README.md"

# Move the file from its original location to the destination:
os.rename(
    src_file, dest_file
)  # Mueve el archivo desde su ubicación original al destino
