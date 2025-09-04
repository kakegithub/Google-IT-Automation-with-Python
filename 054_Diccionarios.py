###################################################################################

x = {}
print(type(x))  # Imprime el tipo de 'x', que es un diccionario.
# <class 'dict'>

# --- Creación de un diccionario con conteo de archivos por extensión ---
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print(file_counts)  # Imprime el diccionario file_counts.
# {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23}

# --- Acceder al valor asociado a la clave "txt" ---
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print(file_counts["txt"])  # Imprime el valor asociado a la clave "txt".
# 14

# --- Comprobar si una clave existe en el diccionario ---
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print("jpg" in file_counts)  # Comprueba si "jpg" es una clave en file_counts.
print("html" in file_counts)  # Comprueba si "html" es una clave en file_counts.
# True
# False

# --- Agregar un nuevo par clave-valor al diccionario ---
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
file_counts["cfg"] = 8  # Agrega la clave "cfg" con el valor 8.
print(file_counts)  # Imprime el diccionario actualizado.
# {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23, 'cfg': 8}

# --- Modificar el valor asociado a una clave existente ---
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
file_counts["csv"] = 17  # Modifica el valor de la clave "csv" a 17.
print(file_counts)  # Imprime el diccionario con el valor modificado.
# {'jpg': 10, 'txt': 14, 'csv': 17, 'py': 23}

# --- Eliminar un par clave-valor del diccionario ---
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23, "cfg": 8}
del file_counts["cfg"]  # Elimina la clave "cfg" y su valor asociado.
print(file_counts)  # Imprime el diccionario sin la clave eliminada.
# {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23}

# --- Iterar sobre las claves del diccionario ---
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
for extension in file_counts:  # Itera sobre cada clave en el diccionario.
    print(extension)  # Imprime la clave actual.
# jpg txt csv py

# --- Iterar sobre los pares clave-valor del diccionario ---
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
for ext, amount in file_counts.items():  # Itera sobre cada par clave-valor.
    print(
        "There are {} files with the .{} extension".format(amount, ext)
    )  # Imprime un mensaje con la cantidad y la extensión.
# There are 10 files with the .jpg extension
# There are 14 files with the .txt extension
# There are 2 files with the .csv extension
# There are 23 files with the .py extension

# --- Obtener las claves y los valores del diccionario ---
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print(file_counts.keys())  # Imprime las claves del diccionario.
print(file_counts.values())  # Imprime los valores del diccionario.
# dict_keys(['jpg', 'txt', 'csv', 'py'])
# dict_values([10, 14, 2, 23])

# --- Iterar sobre los valores del diccionario ---
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
for value in file_counts.values():  # Itera sobre cada valor en el diccionario.
    print(value)  # Imprime el valor actual.
# 10
# 14
# 2
# 23

# --- Función para contar la frecuencia de cada letra en un texto ---
def count_letters(text):
    """
    Cuenta la frecuencia de cada letra en un texto.
    Args:
        text (str): El texto a analizar.
    Returns:
        dict: Un diccionario donde las claves son las letras y los valores son sus frecuencias.
    """
    result = {}  # Inicializa un diccionario vacío para almacenar los resultados.
    for letter in text:  # Itera sobre cada letra en el texto.
        if letter not in result:  # Si la letra no está en el diccionario,
            result[letter] = 0  # la agrega con una frecuencia inicial de 0.
        result[letter] += 1  # Incrementa la frecuencia de la letra en 1.
    return result  # Devuelve el diccionario con las frecuencias de las letras.


print(count_letters("aaaaa"))
print(count_letters("tenant"))
print(count_letters("a long string with a lot of letters"))
# {'a': 5}
# {'t': 2, 'e': 1, 'n': 2, 'a': 1}
# {
#     'a': 2,
#     ' ': 7,
#     'l': 3,
#     'o': 3,
#     'n': 2,
#     'g': 2,
#     's': 2,
#     't': 5,
#     'r': 2,
#     'i': 2,
#     'w': 1,
#     'h': 1,
#     'f': 1,
#     'e': 2,
# }

# --- Comprobar si una clave existe en un diccionario y realizar acciones ---
myDictionary = {}  # Inicializa un diccionario vacío.
# Comprueba si una clave existe en el diccionario y realiza diferentes acciones basadas en el resultado
key = "banana"  # Define la clave a buscar.
if key in myDictionary:  # Comprueba si la clave está en el diccionario.
    print(f"The value of {key} is {myDictionary[key]}")  # Imprime el valor si la clave existe.
else:  # Si la clave no existe,
    print(f"{key} is not found in the dictionary")  # imprime un mensaje indicando que no se encontró.
# banana is not found in the dictionary

# --- Sintaxis y operaciones comunes de diccionarios ---
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

# --- Ejemplo de diccionario con listas como valores ---
pet_dictionary = {
    "dogs": ["Yorkie", "Collie", "Bulldog"],
    "cats": ["Persian", "Scottish Fold", "Siberian"],
    "rabbits": ["Angora", "Holland Lop", "Harlequin"],
}


print(pet_dictionary.get("dogs", 0))  # Imprime la lista de perros del diccionario.
# Should print ['Yorkie', 'Collie', 'Bulldog']

# --- Comparación entre diccionarios y listas ---
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

# Sólo listas:

#     son conjuntos ordenados;

#     acceden a los elementos de la lista por posiciones de índice;

#     requieren que estos índices sean enteros;

#     utilizan corchetes [ ];

#     utilizan comas para separar cada elemento de la lista.
