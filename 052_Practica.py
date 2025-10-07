# --- Habilidades de codificación ---

# Grupo de destrezas 1:
# Utilizar un bucle for para modificar elementos de una lista.
# Utilizar el método list.append().
# Utilizar los métodos string.endswith() y string.replace() para modificar los elementos de una lista.

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
        # Reemplazar "2023" con "2024" si es el caso.
        new = year.replace("2023", "2024")
        # Añadir el año actualizado a la nueva lista.
        updated_years.append(new)
    else:
        # Si no termina con "2023", añadir el año original a la nueva lista.
        updated_years.append(year)

print(updated_years)
# Resultado esperado: ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]

# --- Grupo de destrezas 2 ---
# Utilizar una comprensión de lista para devolver valores.

# Esta función crea una lista de números al cuadrado (n*n) utilizando una comprensión de lista.


def squares(start, end):
    # Calcular el cuadrado de cada número en el rango [start, end] (inclusive).
    return [n * n for n in range(start, end + 1)]


print(squares(2, 3))  # Resultado esperado: [4, 9]
print(squares(1, 5))  # Resultado esperado: [1, 4, 9, 16, 25]
# Resultado esperado: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(squares(0, 10))

# --- Grupo de destrezas 3 ---
# Utilizar una comprensión de lista para modificar elementos de una lista.
# Utilizar el método string.replace() dentro de una comprensión de lista.
# Utilizar el método string[index] dentro de una comprensión de lista.

# Este bloque de código también cambia el año en una lista de fechas, pero utilizando una comprensión de lista.
years = [
    "January 2023",
    "May 2025",
    "April 2023",
    "August 2024",
    "September 2025",
    "December 2023",
]

# Utilizar una comprensión de lista para actualizar los años.
updated_years = [
    year.replace("2023", "2024") if year[-4:] == "2023" else year for year in years
]

print(updated_years)
# Resultado esperado: ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]

# --- Grupo de destrezas 4 ---
# Utilizar el método string.split() para separar una cadena en una lista de palabras individuales.
# Iterar sobre la nueva lista utilizando un bucle for.
# Modificar cada elemento de la lista cortando la cadena del elemento en una posición de índice [1:] dada y añadiendo la subcadena al final del elemento.
# Convierte de nuevo una lista en una cadena.

# Esta función divide una cadena en una lista de palabras, modifica cada palabra moviendo el primer carácter al final, y luego une la lista de nuevo en una cadena.


def change_string(given_string):
    # Inicializar la nueva cadena.
    new_string = ""

    # Dividir la cadena en una lista de palabras.
    new_list = given_string.split()

    # Iterar sobre cada palabra en la lista.
    for element in new_list:
        # Modificar la palabra y añadirla a la nueva cadena.
        new_string += element[1:] + "-" + element[0] + " "

    # Devolver la nueva cadena.
    return new_string


print(
    change_string("1one 2two 3three 4four 5five")
)  # Resultado esperado: "one-1 two-2 three-3 four-4 five-5 "

# --- Grupo de destrezas 5 ---
# Utilice el método string.join() para concatenar una cadena que proporciona un nombre de lista y sus elementos.

# Esta función acepta un nombre de lista y una lista de elementos, y devuelve una cadena con el formato: "The "list_name" list includes: element1, element2, element3".


def list_elements(list_name, elements):
    # Concatenar la cadena con el nombre de la lista y los elementos.
    return "The " + list_name + " list includes: " + ", ".join(elements)


print(
    list_elements(
        "Printers", ["Color Printer", "Black and White Printer", "3-D Printer"]
    )
)
# Resultado esperado: "The Printers list includes: Color Printer, Black and White Printer, 3-D Printer"

# --- Grupo de destrezas 6 ---
# Utilice map() y convierta el objeto map en una lista para poder imprimir todos los resultados a la vez.

# Una función simple para añadir 1 a un número dado.


def add_one(number):
    return number + 1


# Una lista de números.
numbers = [1, 2, 3, 4, 5]

# Utilizar map para aplicar la función a cada elemento de la lista.
result = map(add_one, numbers)

# Convertir el objeto map a una lista para imprimir el resultado.
print(list(result))
# Resultado esperado: [2, 3, 4, 5, 6]
