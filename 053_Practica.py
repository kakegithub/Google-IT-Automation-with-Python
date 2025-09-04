# --- Conversión de lista a tupla ---
# El operador tuple() se utiliza para convertir un iterable (como una lista, una cadena o un conjunto) en una tupla.

# Convertir una lista a una tupla
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)

print(my_tuple)  # Imprime: (1, 2, 3, 4)

# Aunque los paréntesis se utilizan a menudo para definir una tupla, no siempre son necesarios.
# La siguiente sintaxis también es válida:

my_tuple = 1, 2, 3, 4
print(my_tuple)  # Imprime: (1, 2, 3, 4)

# --- Tuplas con objetos mutables ---

# Una tupla con una lista como elemento
my_tuple = (1, 2, ["a", "b", "c"])

# No se puede cambiar la tupla en sí
# my_tuple[0] = 3  # Esto generaría un TypeError

# Pero se pueden modificar los elementos mutables dentro de la tupla
my_tuple[2][0] = "x"
print(my_tuple)  # Imprime: (1, 2, ['x', 'b', 'c'])

# --- Devolución de múltiples valores desde funciones ---
# Ejemplo de función que devuelve múltiples valores como una tupla
def calculate_numbers(a, b):
    """
    Calcula la suma, resta, multiplicación y división de dos números.
    Args:
        a: El primer número.
        b: El segundo número.
    Returns:
        Una tupla que contiene la suma, resta, multiplicación y división de a y b.
    """
    return a + b, a - b, a * b, a / b


result = calculate_numbers(10, 2)
print(result)  # Imprime: (12, 8, 20, 5.0)


# Desempaquetado de los valores devueltos por la función
def calculate_numbers(a, b):
    """
    Calcula la suma, resta, multiplicación y división de dos números.
    Args:
        a: El primer número.
        b: El segundo número.
    Returns:
        Una tupla que contiene la suma, resta, multiplicación y división de a y b.
    """
    return a + b, a - b, a * b, a / b


add_result, sub_result, mul_result, div_result = calculate_numbers(10, 2)
print(add_result)  # Imprime: 12
print(sub_result)  # Imprime: 8

# --- Comprensión de listas ---
# [expresión para variable en secuencia]
my_list = [x * 2 for x in range(1, 11)]

# [expresión para variable en secuencia si condición]
my_list = [x for x in range(1, 101) if x % 10 == 0]

# --- Modificación de una lista de fechas ---
# Este bloque de código cambia el año en una lista de fechas.
years = [
    "January 2023",
    "May 2025",
    "April 2023",
    "August 2024",
    "September 2025",
    "December 2023",
]

# Inicializar la lista para los años actualizados.
updated_years = []
# Iterar sobre cada año en la lista.
for year in years:
    # Comprobar si el año termina con "2023".
    if year.endswith("2023"):
        # Si es así, reemplazar "2023" con "2024".
        new = year.replace("2023", "2024")
        # Añadir el año actualizado a la nueva lista.
        updated_years.append(new)
    else:
        # Si no termina con "2023", añadir el año original a la nueva lista.
        updated_years.append(year)

print(updated_years)
# Imprime: ['January 2024', 'May 2025', 'April 2024', 'August 2024', 'September 2025', 'December 2024']

# --- Creación de una lista de números al cuadrado ---
# Esta función crea una lista de números al cuadrado (n*n).
def squares(start, end):
    """
    Calcula el cuadrado de cada número en el rango [start, end] (inclusive).
    Args:
        start: El número inicial del rango.
        end: El número final del rango.
    Returns:
        Una lista con los cuadrados de los números en el rango [start, end].
    """
    # La comprensión de lista calcula el cuadrado de cada número en el rango.
    return [n * n for n in range(start, end + 1)]


print(squares(2, 3))  # Imprime: [4, 9]
print(squares(1, 5))  # Imprime: [1, 4, 9, 16, 25]
print(squares(0, 10))  # Imprime: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# --- Modificación de una lista de fechas con comprensión de lista ---
# Este bloque de código también cambia el año en una lista de fechas, pero utilizando una comprensión de lista.
years = [
    "January 2023",
    "May 2025",
    "April 2023",
    "August 2024",
    "September 2025",
    "December 2023",
]

# La comprensión de lista crea una nueva lista "updated_years" con los años actualizados.
updated_years = [
    year.replace("2023", "2024") if year[-4:] == "2023" else year for year in years
]

print(updated_years)
# Imprime: ['January 2024', 'May 2025', 'April 2024', 'August 2024', 'September 2025', 'December 2024']

# --- Modificación de una cadena ---
# Esta función divide una cadena en una lista de elementos, modifica cada elemento moviendo el primer carácter al final,
# y añade un guión entre el elemento y el carácter movido.
def change_string(given_string):
    """
    Divide una cadena en una lista de palabras, modifica cada palabra moviendo el primer carácter al final,
    y luego une la lista de nuevo en una cadena.
    Args:
        given_string: La cadena a modificar.
    Returns:
        La cadena modificada.
    """
    # Inicializar "new_string" como una cadena vacía.
    new_string = ""

    # Dividir la "given_string" en una "new_list", con cada "element" conteniendo una palabra de la cadena.
    new_list = given_string.split()

    # El bucle for itera sobre cada "element" en la "new_list".
    for element in new_list:
        # Convertir la lista en una "new_string" concatenando los siguientes elementos:
        # + Cada "element" de la lista (empezando en la posición de índice [1:]),
        # + un guión "-",
        # + el primer carácter del "element" (usando el índice [0]) al final del "element", y finalmente,
        # + un espacio " " para separar cada "element" en la "new_string".
        new_string += element[1:] + "-" + element[0] + " "

    # Devolver la lista que ha sido convertida de nuevo en una cadena.
    return new_string


print(
    change_string("1one 2two 3three 4four 5five")
)  # Imprime: "one-1 two-2 three-3 four-4 five-5 "

# --- Creación de una cadena con el nombre de una lista y sus elementos ---
# Esta función acepta un nombre de lista y una lista de elementos, y devuelve una cadena con el formato:
# "The "list_name" list includes: element1, element2, element3".
def list_elements(list_name, elements):
    """
    Acepta un nombre de lista y una lista de elementos, y devuelve una cadena con el formato:
    "The "list_name" list includes: element1, element2, element3".
    Args:
        list_name: El nombre de la lista.
        elements: La lista de elementos.
    Returns:
        Una cadena con el formato especificado.
    """
    # Concatenar la cadena con el nombre de la lista y los elementos.
    return "The " + list_name + " list includes: " + ", ".join(elements)


print(
    list_elements(
        "Printers", ["Color Printer", "Black and White Printer", "3-D Printer"]
    )
)
# Imprime: "The Printers list includes: Color Printer, Black and White Printer, 3-D Printer"

# --- Uso de map() para añadir 1 a cada elemento de una lista ---
# Una función simple para añadir 1 a un número dado
def add_one(number):
    """
    Añade 1 a un número dado.
    Args:
        number: El número al que se le añadirá 1.
    Returns:
        El número incrementado en 1.
    """
    return number + 1


# Una lista de números
numbers = [1, 2, 3, 4, 5]

# Usar map para aplicar la función a cada elemento de la lista
result = map(add_one, numbers)

# Convertir el objeto map a una lista para imprimir el resultado
print(list(result))
# Imprime: [2, 3, 4, 5, 6]

# --- Combinación de dos listas con zip() ---
# Dos listas
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Usar zip para combinar las listas
combined = zip(names, ages)

# Convertir el objeto zip a una lista para imprimir el resultado
print(list(combined))
# Imprime: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# --- Modificación de nombres de archivo ---
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generar new_filenames como una lista que contiene los nuevos nombres de archivo
# usando tantas líneas de código como requiera el método elegido.


new_filenames = []
for filename in filenames:
    if filename.endswith("hpp"):
        new = filename.replace(".hpp", ".h")
        new_filenames.append(new)
    else:
        new_filenames.append(filename)


print(new_filenames)
# Imprime: ['program.c', 'stdio.h', 'sample.h', 'a.out', 'math.h', 'hpp.out']

# --- Modificación de nombres de archivo con comprensión de lista ---
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generar new_filenames como una lista que contiene los nuevos nombres de archivo
# usando tantas líneas de código como requiera el método elegido.
new_filenames = [
    filename.replace(".hpp", ".h") if filename.endswith(".hpp") else filename
    for filename in filenames
]  # Iniciar el código aquí


print(new_filenames)
# Imprime: ['program.c', 'stdio.h', 'sample.h', 'a.out', 'math.h', 'hpp.out']

# --- Conversión de una frase a Pig Latin ---
def pig_latin(text):
    """
    Convierte una frase a Pig Latin.
    Args:
        text: La frase a convertir.
    Returns:
        La frase convertida a Pig Latin.
    """
    say = ""
    # Separar el texto en palabras
    words = text.split()
    for word in words:
        # Crear la palabra en Pig Latin y añadirla a la lista
        pig_word = word[1:] + word[0] + "ay"
        say += pig_word + " "
        # Convertir la lista de nuevo en una frase
    return say.strip()


print(pig_latin("hello how are you"))  # Imprime: "ellohay owhay reaay ouyay"
print(
    pig_latin("programming in python is fun")
)  # Imprime: "rogrammingpay niay ythonpay siay unfay"

# --- Creación de biografías ---
def biography_list(people):
    """
    Imprime una biografía para cada persona en la lista.
    Args:
        people: Una lista de tuplas, donde cada tupla contiene el nombre, la edad y la profesión de una persona.
    """
    # Iterar sobre cada "person" en la lista "people" de tuplas.
    for person in people:

        # Separar los 3 elementos en cada tupla en 3 variables:
        # "name", "age", y "profession"
        name, edad, profession = person

        # Formatear la frase requerida y colocar las 3 variables
        # en los marcadores de posición correctos usando el método .format().
        print("{} is {} years old and works as {}".format(name, edad, profession))


# Llamada a la función:
biography_list(
    [("Ira", 30, "a Chef"), ("Raj", 35, "a Lawyer"), ("Maria", 25, "an Engineer")]
)

# El resultado debería coincidir con:
# Ira is 30 years old and works as a Chef
# Raj is 35 years old and works as a Lawyer
# Maria is 25 years old and works as an Engineer
