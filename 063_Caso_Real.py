# #  Cada mes, le entregan una hoja de cálculo con cientos de nuevas contrataciones. Se le pide que cree cuentas de usuario para todos ellos en un servidor Linux.
#     Leer una lista de nuevas contrataciones de users_in.csv.

#     Generar contraseñas aleatorias de 16 caracteres para cada usuario.

#     Crear cada cuenta de usuario.

#     Volver a escribir la hoja de cálculo en users_out.csv con las nuevas contraseñas.

import csv
import secrets
import subprocess
from pathlib import Path  # to locate the data files

cwd = Path.cwd() / "drive/MyDrive/Colab Notebooks"
with open(cwd / "data/users_in.csv", "r") as file_input, open(
    cwd / "data/users_out.csv", "w"
) as file_output:
    reader = csv.DictReader(file_input)
    reader = csv.DictReader(file_input)
writer = csv.DictWriter(file_output, fieldnames=reader.fieldnames)
writer.writeheader()
    for user in reader:
    user["password"] = secrets.token_hex(8)
        useradd_cmd = ["/sbin/useradd",
            "-c", user["real_name"],
                "-m",
                       "-G", "users",
                       "-p", user["password"],
                       user["username"]]
        subprocess.run(useradd_cmd, check=True)
    writer.writerow(user)