import re
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])

# Muestra el nombre reordenado en el formato "Nombre Apellido"
print("{} {}".format(result[2], result[1]))
