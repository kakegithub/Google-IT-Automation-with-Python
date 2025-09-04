# Cada mes, le entregan una hoja de cálculo con cientos de nuevas contrataciones. Se le pide que cree cuentas de usuario para todos ellos en un servidor Linux. El formato de la hoja de cálculo es el siguiente:
# username,password,real_name
# amanda,,Amanda Alonso
# ian,,Ian Ortega
# eugene,,Eugene Konya
# [...]
# Observa que el campo de contraseña está vacío para todos los registros. Esto significa que necesitas generar contraseñas aleatorias para cada usuario y luego crear sus cuentas. También querrás escribir las contraseñas que generes en un nuevo Archivo CSV para que puedas indicar sus contraseñas a los nuevos empleados.
# Esta tarea no es difícil, pero requiere mucho tiempo si tienes que crear contraseñas y cuentas para los cientos de nuevos empleados uno por uno. La solución es automatizar esta tarea en Python.

# El script
# Para automatizar la tarea de crear contraseñas y cuentas para todos estos nuevos empleados, el script debería hacer lo siguiente:
#     Leer una lista de nuevas contrataciones de users_in.csv.
#     Generar contraseñas aleatorias de 16 caracteres para cada usuario.
#     Crear cada cuenta de usuario.
#     Volver a escribir la hoja de cálculo en users_out.csv con las nuevas contraseñas.

# Tus herramientas
# Para ayudar a organizar todos los datos, crear cuentas para los nuevos empleados y crear contraseñas para cada nuevo usuario, primero necesitas importar algunas bibliotecas estándar de Python.

import csv  # Esta biblioteca ayuda a leer y escribir los Archivos CSV.
import secrets  # Esto ayuda a generar contraseñas aleatorias para cada cuenta de usuario.
import subprocess  # Esto llama al comando useradd, que crea y añade cada cuenta de usuario.
from pathlib import Path  # to locate the data files # Esta biblioteca ayuda a localizar los archivos de datos para cada cuenta de usuario.

# Después de importar las bibliotecas que le ayudan a ejecutar su script, necesita obtener el directorio de trabajo actual y encontrar el subdirectorio donde se almacenan los archivos CSV. Utilice cwd para "directorio de trabajo actual" e identifique la ruta del directorio Python como una cadena:
# cwd = Path.cwd() / "drive/MyDrive/Colab Notebooks"
# A continuación, utiliza una sentencia with y una palabra clave as. La sentencia with ayuda con la gestión de recursos, y la palabra clave as crea un alias para el recurso que desea llamar. Considere el siguiente código:
# with open(cwd / "data/users_in.csv", "r") as file_input, open(cwd / "data/users_out.csv", "w") as file_output:
# La biblioteca CSV se encarga de leer y analizar la entrada del archivo.
# A continuación, puede utilizar un objeto DictReader para que cada fila del archivo se lea en un dict() con los nombres y valores de los campos, de la siguiente manera: {"username": "amanda", "password": "", "real_name": "Amanda Alonso"}.
# El siguiente código es un ejemplo de cómo se utiliza el DictReader:
#     reader = csv.DictReader(file_input)
# ¡La entrada para el script ya está completa! Ahora necesita configurar la salida. Cree un DictWriter y utilice los mismos nombres de campo de la entrada, como se muestra a continuación:
# writer = csv.DictWriter(file_output,fieldnames=reader.fieldnames)
#      writer.writeheader()
# ahora, crea un bucle for para recorrer cada registro del archivo de entrada.
# for user in reader:
# Después del bucle for, utiliza el secrets library que importó al principio del script para generar una contraseña aleatoria de ocho bytes hexadecimales, lo que equivale a 16 caracteres en total. A continuación, ejecuta el comando /sbin/useradd para crear cada usuario. El parámetro check=True hace que el script salga con un CalledProcessError si el comando falla por alguna razón.
# user["password"] = secrets.token_hex(8)
#         useradd_cmd = ["/sbin/useradd",
#                        "-c", user["real_name"],
#                        "-m",
#                        "-G", "users",
#                        "-p", user["password"],
#                        user["username"]]
#         subprocess.run(useradd_cmd, check=True)
# Por último, vuelve a escribir los registros en el archivo de salida, incluidas las contraseñas. Al ejecutar el código, las nuevas cuentas de usuario y sus contraseñas se generan en un nuevo Archivo CSV.
#     writer.writerow(user)
# Una vez ejecutado el script, Tendremos el Archivo CSV

def create_users(input_csv, output_csv):
    """
    Lee un archivo CSV de entrada, genera contraseñas aleatorias para cada usuario,
    crea las cuentas de usuario en el sistema y escribe los resultados en un archivo CSV de salida.

    Args:
        input_csv (str): La ruta al archivo CSV de entrada.
        output_csv (str): La ruta al archivo CSV de salida.
    """
    cwd = Path.cwd()  # Obtiene el directorio de trabajo actual

    try:
        with open(cwd / "data" / input_csv, "r") as file_input, open(
            cwd / "data" / output_csv, "w", newline=""
        ) as file_output:
            reader = csv.DictReader(file_input)  # Crea un DictReader para leer el archivo CSV de entrada
            writer = csv.DictWriter(
                file_output, fieldnames=reader.fieldnames
            )  # Crea un DictWriter para escribir en el archivo CSV de salida
            writer.writeheader()  # Escribe la cabecera en el archivo CSV de salida

            for user in reader:  # Itera sobre cada fila del archivo CSV de entrada
                user["password"] = secrets.token_hex(
                    8
                )  # Genera una contraseña aleatoria de 16 caracteres
                useradd_cmd = [  # Define el comando para crear el usuario en Linux
                    "/sbin/useradd",
                    "-c",
                    user["real_name"],
                    "-m",
                    "-G",
                    "users",
                    "-p",
                    user["password"],
                    user["username"],
                ]
                try:
                    subprocess.run(
                        useradd_cmd, check=True
                    )  # Ejecuta el comando para crear el usuario
                    print(f"Usuario {user['username']} creado con éxito.")
                except subprocess.CalledProcessError as e:
                    print(f"Error al crear el usuario {user['username']}: {e}")

                writer.writerow(
                    user
                )  # Escribe la información del usuario (incluyendo la contraseña) en el archivo CSV de salida

    except FileNotFoundError:
        print(
            "Error: El archivo users_in.csv no se encuentra en el directorio 'data'."
        )
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


# Ejemplo de uso (descomentar para ejecutar):
# create_users("users_in.csv", "users_out.csv")
