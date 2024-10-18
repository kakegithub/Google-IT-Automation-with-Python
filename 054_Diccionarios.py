###################################################################################

x = {}
type(x)
# <class 'dict'>
#####################################################################################

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print(file_counts)

# {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23}

#######################################################################################

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
file_counts["txt"]

# 14

######################################################################################

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
"jpg" in file_counts
"html" in file_counts

# False

########################################################################################

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
file_counts["cfg"] = 8
print(file_counts)

# {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23, 'cfg': 8}

########################################################################################

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
file_counts["csv"] = 17
print(file_counts)

# {'jpg': 10, 'txt': 14, 'csv': 17, 'py': 23}

#########################################################################################

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23, "cfg": 8}
del file_counts["cfg"]
print(file_counts)

# {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23}

##########################################################################################

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
for extension in file_counts:
    print(extension)

# jpg txt csv py

#############################################################################################

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
for ext, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount, ext))

# There are 10 files with the .jpg extension
# There are 14 files with the .txt extension
# There are 2 files with the .csv extension
# There are 23 files with the .py extension

##############################################################################################

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
file_counts.keys()
file_counts.values()

# dict_values([10, 14, 2, 23])

################################################################################################

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
for value in file_counts.values():
    print(value)

# 10
# 14
# 2
# 23

####################################################################################################


def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


count_letters("aaaaa")
count_letters("tenant")
count_letters("a long string with a lot of letters")

# {
#     "a": 2,
#     " ": 7,
#     "l": 3,
#     "o": 3,
#     "n": 2,
#     "g": 2,
#     "s": 2,
#     "t": 5,
#     "r": 2,
#     "i": 2,
#     "w": 1,
#     "h": 1,
#     "f": 1,
#     "e": 2,
# }

#########################################################################################

myDictionary = {}
# Check if a key exists in the dictionary and perform different actions based on the result
key = "banana"
if key in myDictionary:
    print(f"The value of {key} is {myDictionary[key]}")
else:
    print(f"{key} is not found in the dictionary")

############################################################################################


# Sintaxis
my_dictionary = {"keyA": ["value1", "value2"], "keyB": ["value3", "value4"]}

# Operaciones

#     len(diccionario) - Devuelve el número de elementos de un diccionario.

#     for clave, en diccionario - Itera sobre cada clave de un diccionario.

#     for key, value in dictionary.items() - Recorre cada par clave,valor de un diccionario.

#     if clave en diccionario - Comprueba si una clave está en un diccionario.

#     dictionary[key] - Accede a un valor utilizando la clave asociada de un diccionario.

#     dictionary[key] = value - Establece un valor asociado a una clave.

#     del dictionary[key] - Elimina de un diccionario un valor que utiliza la clave asociada.


# Métodos

#     dictionary.get(key, default) - Devuelve el valor correspondiente a una clave, o el valor por defecto si la clave especificada no está presente.

#     dictionary.keys() - Devuelve una secuencia que contiene las claves de un diccionario.

#     dictionary.values() - Devuelve una secuencia que contiene los valores de un diccionario.

#     dictionary[key].append(value) - Añade un nuevo valor a una clave existente.

#     diccionario.actualizar(otro_diccionario) - Actualiza un diccionario con los elementos de otro diccionario. Las entradas existentes se actualizan; las nuevas se añaden.

#     dictionary.clear() - Elimina todos los elementos de un diccionario.

#     dictionary.copy() - Hace una copia de un diccionario.

####################################################################################################################################3

pet_dictionary = {
    "dogs": ["Yorkie", "Collie", "Bulldog"],
    "cats": ["Persian", "Scottish Fold", "Siberian"],
    "rabbits": ["Angora", "Holland Lop", "Harlequin"],
}


print(pet_dictionary.get("dogs", 0))
# Should print ['Yorkie', 'Collie', 'Bulldog']

##################################################################################################################

# Diccionarios frente a listas

# Los diccionarios son similares a las listas, pero existen algunas diferencias:
# Tanto los diccionarios como las listas

#     se utilizan para organizar elementos en colecciones;

#     se utilizan para inicializar un nuevo diccionario o lista, utilizan paréntesis vacíos;

#     pueden iterar a través de los ítems o elementos de la colección; y

#     pueden utilizar diversos métodos y operaciones para crear y modificar las colecciones, como eliminar e insertar elementos.

# Sólo los diccionarios

#     son conjuntos desordenados

#     tienen claves que pueden ser de distintos tipos de datos, como cadenas, enteros, flotantes o tuplas;.

#     puede acceder a los valores del diccionario mediante claves;

#     utilizar corchetes dentro de llaves { [ ] };

#     utilice dos puntos entre la clave y el/los valor(es);

#     utilice comas para separar cada grupo de claves y cada valor dentro de un grupo de claves;

#     hacen que sea más rápido y fácil para un intérprete de Python encontrar elementos específicos, en comparación con una lista.

# ##########################################################################################################################################

# Sólo listas:

#     son conjuntos ordenados;

#     acceden a los elementos de la lista por posiciones de índice;

#     requieren que estos índices sean enteros;

#     utilizan corchetes [ ];

#     utilizan comas para separar cada elemento de la lista.
