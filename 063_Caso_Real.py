# Cada mes, le entregan una hoja de cálculo con cientos de nuevas contrataciones. Se le pide que cree cuentas de usuario para todos ellos en un servidor Linux.
#     Leer una lista de nuevas contrataciones de users_in.csv.
#     Generar contraseñas aleatorias de 16 caracteres para cada usuario.
#     Crear cada cuenta de usuario.
#     Volver a escribir la hoja de cálculo en users_out.csv con las nuevas contraseñas.

import csv  # Importa la biblioteca csv para trabajar con archivos CSV
import secrets  # Importa la biblioteca secrets para generar contraseñas seguras
import subprocess  # Importa la biblioteca subprocess para ejecutar comandos del sistema
from pathlib import Path  # Importa la biblioteca pathlib para manipular rutas de archivos

# Define la ruta al directorio de trabajo actual (esto puede necesitar ser ajustado según tu entorno)
cwd = Path.cwd() / "drive/MyDrive/Colab Notebooks"

# Abre los archivos de entrada y salida utilizando un bloque "with" para asegurar que se cierren correctamente después de su uso
with open(cwd / "data/users_in.csv", "r") as file_input, open(
    cwd / "data/users_out.csv", "w", newline=""
) as file_output:
    # Crea un objeto DictReader para leer el archivo CSV de entrada como un diccionario
    reader = csv.DictReader(file_input)
    # Crea un objeto DictWriter para escribir en el archivo CSV de salida, utilizando los mismos nombres de campo que el archivo de entrada
    writer = csv.DictWriter(file_output, fieldnames=reader.fieldnames)
    # Escribe la fila de encabezado en el archivo CSV de salida
    writer.writeheader()

    # Itera sobre cada fila (usuario) en el archivo CSV de entrada
    for user in reader:
        # Genera una contraseña aleatoria de 16 caracteres (8 bytes hexadecimales)
        user["password"] = secrets.token_hex(8)
        # Define el comando para crear el usuario en el sistema Linux
        useradd_cmd = [
            "/sbin/useradd",
            "-c",
            user["real_name"],
            "-m",  # Crea el directorio home del usuario
            "-G",
            "users",  # Agrega el usuario al grupo "users"
            "-p",
            user["password"],  # Establece la contraseña del usuario (¡ADVERTENCIA: esto no es seguro en la práctica!)
            user["username"],  # Nombre de usuario
        ]
        # Ejecuta el comando useradd utilizando subprocess.run y verifica si la ejecución fue exitosa
        try:
            subprocess.run(useradd_cmd, check=True)
            print(f"Usuario {user['username']} creado con éxito.")
        except subprocess.CalledProcessError as e:
            print(f"Error al crear el usuario {user['username']}: {e}")
        # Escribe la información del usuario (incluyendo la contraseña generada) en el archivo CSV de salida
        writer.writerow(user)