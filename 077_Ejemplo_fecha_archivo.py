"""La función fecha_archivo crea un nuevo archivo en el directorio de trabajo actual, comprueba la fecha en que se modificó el archivo y devuelve sólo la parte de fecha de la marca de tiempo en el formato aaaa-mm-dd."""

import os
import datetime


def file_date(filename):
    # Create the file in the current directory
    with open(filename, "w") as file:
        timestamp = os.path.getmtime(filename)
    # Convert the timestamp into a readable format, then into a string
    mtime = datetime.datetime.fromtimestamp(timestamp)
    # Return just the date portion
    # Hint: how many characters are in “yyyy-mm-dd”?
    return "{}".format(mtime.strftime("%Y-%m-%d"))


print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd
