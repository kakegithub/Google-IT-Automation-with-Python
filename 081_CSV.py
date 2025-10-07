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


# Define una lista de diccionarios, donde cada diccionario representa un usuario con su nombre, nombre de usuario y departamento.
users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
 {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
  {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
# Define una lista de cadenas que se utilizarán como encabezados (nombres de campo) para las columnas del archivo CSV.
keys = ["name", "username", "department"]
# Abre el archivo 'by_department.csv' en modo escritura ('w'). El 'with' asegura que el archivo se cierre automáticamente.
with open('by_department.csv', 'w') as by_department:
    # Crea un objeto DictWriter, que mapea diccionarios a filas CSV. 'fieldnames' especifica los encabezados de las columnas.
    writer = csv.DictWriter(by_department, fieldnames=keys)
    # Escribe la fila de encabezado en el archivo CSV.
    writer.writeheader()
    # Escribe todas las filas (diccionarios) de la lista 'users' en el archivo CSV.
    writer.writerows(users)

#the following command should be used in the terminal

# cat by_department.csv  