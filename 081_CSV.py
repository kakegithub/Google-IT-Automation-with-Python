import csv  # Importa el módulo csv para trabajar con archivos CSV

"""
Script de ejemplo:
Lee "software.csv" y muestra por pantalla "<name> has <users> users" para cada fila.
Utiliza csv.DictReader para mapear cada columna por su nombre de cabecera.
"""

# Ejemplo del contenido esperado en software.csv:
# name,version,status,users
# MailTree,5.34,production,324
# CalDoor,1.25.1,beta,22
# Chatty Chicken,0.34,alpha,4

# Abrimos el archivo CSV en modo lectura.
# Nota: en Windows se recomienda abrir con newline='' para evitar líneas en blanco extra
# y especificar encoding si es necesario, por ejemplo: open("software.csv", newline='', encoding='utf-8')
with open("software.csv") as software:
    # DictReader interpreta la primera fila como cabecera y devuelve cada fila como un dict
    # con claves 'name', 'version', 'status', 'users'.
    reader = csv.DictReader(software)

    # Iteramos sobre cada fila del CSV
    for row in reader:
        # 'row' es un diccionario; accedemos a 'name' y 'users' para formatear la salida.
        # Usamos str.format para mantener compatibilidad con versiones antiguas de Python.
        print("{} has {} users".format(row["name"], row["users"]))  # Imprime el nombre del software y el número de usuarios
