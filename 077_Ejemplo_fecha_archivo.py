"""La función fecha_archivo crea un nuevo archivo en el directorio de trabajo actual,
comprueba la fecha en que se modificó el archivo y devuelve sólo la parte de fecha de la marca de tiempo en el formato aaaa-mm-dd.
"""

import os  # Importa el módulo os para interactuar con el sistema operativo
import datetime  # Importa el módulo datetime para trabajar con fechas y horas


def file_date(filename):
    """
    Crea un nuevo archivo, obtiene su fecha de modificación y devuelve la fecha en formato aaaa-mm-dd.

    Args:
        filename (str): El nombre del archivo a crear.

    Returns:
        str: La fecha de modificación del archivo en formato aaaa-mm-dd.
    """
    # Create the file in the current directory
    with open(filename, "w") as file:  # Abre el archivo en modo escritura
        timestamp = os.path.getmtime(
            filename
        )  # Obtiene la fecha de la última modificación del archivo en segundos desde epoch
    # Convert the timestamp into a readable format, then into a string
    mtime = datetime.datetime.fromtimestamp(
        timestamp
    )  # Convierte la fecha de la última modificación de segundos desde epoch a un objeto datetime
    # Return just the date portion
    # Hint: how many characters are in “yyyy-mm-dd”?
    return "{}".format(
        mtime.strftime("%Y-%m-%d")
    )  # Formatea la fecha como aaaa-mm-dd y la devuelve


print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd
