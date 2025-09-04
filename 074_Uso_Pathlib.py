# Create a directory and move a file from one directory to another
# using Pathlib.

from pathlib import Path  # Importa la clase Path del módulo pathlib

# Check to see if the "test1" subdirectory exists. If not, create it:
dest_dir = Path("./test1/")  # Crea un objeto Path para el directorio de destino "test1"
if not dest_dir.exists():  # Comprueba si el directorio de destino existe
    dest_dir.mkdir()  # Crea el directorio de destino si no existe

# Construct source and destination paths:
src_file = Path("./sample_data/README.md")  # Crea un objeto Path para el archivo de origen "README.md"
dest_file = dest_dir / "README.md"  # Crea un objeto Path para el archivo de destino "README.md" combinando el directorio de destino y el nombre del archivo

# Move the file from its original location to the destination:
src_file.rename(dest_file)  # Renombra (mueve) el archivo desde su ubicación original al destino
