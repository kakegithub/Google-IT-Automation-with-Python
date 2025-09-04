import csv  # Importa el módulo csv para trabajar con archivos CSV

# Define una lista de listas llamada hosts, donde cada sublista contiene el nombre de un host y su dirección IP
hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]

# Abre el archivo 'hosts.csv' en modo escritura ('w') utilizando la declaración 'with' para asegurar que el archivo se cierre correctamente después de su uso
with open('hosts.csv', 'w') as hosts_csv:
    # Crea un objeto escritor CSV para escribir en el archivo abierto
    writer = csv.writer(hosts_csv)
    # Escribe todas las filas de la lista 'hosts' en el archivo CSV
    writer.writerows(hosts)
