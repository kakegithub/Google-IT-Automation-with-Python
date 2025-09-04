# Rellene los espacios en blanco para completar la función "confirmar_longitud".
# Esta función debe devolver cuántos caracteres contiene una cadena siempre que tenga uno o más caracteres,
# de lo contrario devolverá 0.
# Complete las operaciones con cadenas necesarias en esta función para que una entrada como "lunes" produzca la salida "6".
def confirm_length(word):
    """
    Devuelve la longitud de una cadena si tiene uno o más caracteres, de lo contrario devuelve 0.

    Args:
        word (str): La cadena para comprobar su longitud.

    Returns:
        int: La longitud de la cadena si tiene uno o más caracteres, de lo contrario 0.
    """
    # Complete the condition statement using a string operation.
    if len(word) > 0:
        # Complete the return statement using a string operation.
        return len(word)
    else:
        return 0


print(confirm_length("a"))  # Should print 1
print(confirm_length("This is a long string"))  # Should print 21
print(confirm_length("Monday"))  # Should print 6
print(confirm_length(""))  # Should print 0
######################################################################################################################################

# Rellene el espacio en blanco para completar la función "cadena_palabras".
# Esta función debe dividir las palabras de la "cadena" dada y devolver el número de palabras de la "cadena".
# Complete la operación de cadena y el método necesarios en esta función para que una llamada a una función como "cadena_palabras("Hola, mundo")" devuelva la salida "2".
def string_words(string):
    """
    Divide una cadena en palabras y devuelve el número de palabras.

    Args:
        string (str): La cadena para dividir en palabras.

    Returns:
        int: El número de palabras en la cadena.
    """
    # Complete the return statement using both a string operation and
    # a string method in a single line.
    return len(string.split())


print(string_words("Hello, World"))  # Should print 2
print(string_words("Python is awesome"))  # Should print 3
print(string_words("Keep going"))  # Should print 2
print(string_words("Have a nice day"))  # Should print 4

##########################################################################################################################################3

# Considere el siguiente escenario sobre el uso de listas en Python:

# Un profesor encargó a sus dos ayudantes, Jaime y Drew, la tarea de llevar una lista de asistencia de los alumnos por orden de llegada al aula.
# Drew fue el primero en anotar qué alumnos llegaban, y luego Jaime tomó el relevo.
# Después de la clase, cada uno introdujo su lista en el ordenador y la envió por correo electrónico al profesor.
# El profesor quiere combinar las dos listas en una sola, en el orden de llegada de cada alumno.
# Jaime envió un correo electrónico de seguimiento, diciendo que su lista está en orden inverso.

# Complete el código para combinar las dos listas en una en el orden de: el contenido de la lista de Drew, seguido de la lista de Jaime en orden inverso,
# para producir una lista exacta de los estudiantes según fueron llegando.
# Esta función debería

# aceptar dos listas a través de los parámetros de la función;

# invertir el orden de "lista1

# combinar las dos listas de forma que "lista2" vaya primero, seguida de "lista1";

# devolver la nueva lista.
def combine_lists(list1, list2):
    """
    Combina dos listas, invirtiendo la primera lista y añadiéndola a la segunda.

    Args:
        list1 (list): La primera lista para invertir y añadir.
        list2 (list): La segunda lista a la que se añadirá la primera lista invertida.

    Returns:
        list: Una nueva lista que contiene los elementos de list2 seguidos de los elementos de list1 en orden inverso.
    """
    combined_list = []  # Initialize an empty list variable
    list1.reverse()  # Reverse the order of "list1"
    list2.extend(list1)  # Combine the two lists
    combined_list = list2
    return combined_list


Jaimes_list = ["Alma", "Chika", "Benjamin", "Jocelyn", "Oakley"]
Drews_list = ["Minna", "Carol", "Gunnar", "Malena"]


print(combine_lists(Jaimes_list, Drews_list))
# Should print ['Minna', 'Carol', 'Gunnar', 'Malena', 'Oakley', 'Jocelyn', 'Benjamin', 'Chika', 'Alma']

###########################################################################################################################################################

# Rellene el espacio en blanco para completar la función "números_pares".
# Esta función debe utilizar una comprensión de lista para crear una lista de números pares utilizando una sentencia condicional if con el operador módulo para comprobar si hay números divisibles uniformemente por 2.
# La función recibe dos variables y debe devolver la lista de números pares que se encuentren entre las variables "primera" y "última" exclusivamente (es decir, no modificar el comportamiento por defecto del rango para excluir el valor "final" del rango).
# Por ejemplo, números_pares(2, 7) debería devolver [2, 4, 6].
def even_numbers(first, last):
    """
    Devuelve una lista de números pares dentro de un rango especificado.

    Args:
        first (int): El inicio del rango (inclusive).
        last (int): El final del rango (exclusive).

    Returns:
        list: Una lista de números pares dentro del rango especificado.
    """
    return [n for n in range(first, last) if n % 2 == 0]


print(even_numbers(4, 14))  # Should print [4, 6, 8, 10, 12]
print(even_numbers(0, 9))  # Should print [0, 2, 4, 6, 8]
print(even_numbers(2, 7))  # Should print [2, 4, 6]

#######################################################################################################################################################

# Rellene los espacios en blanco para completar la función "países".
# Esta función acepta un diccionario que contiene una lista de continentes (claves) y varios países de cada continente (valores).
# Para cada continente, formatee una cadena para imprimir sólo los nombres de los países.
# Los valores de cada clave deben aparecer en su propia línea.
def countries(countries_dict):
    """
    Formatea una cadena para imprimir los nombres de los países de cada continente.

    Args:
        countries_dict (dict): Un diccionario donde las claves son los continentes y los valores son listas de países.

    Returns:
        str: Una cadena formateada que contiene los nombres de los países de cada continente, cada uno en su propia línea.
    """
    result = ""
    # Complete the for loop to iterate through the key and value items
    # in the dictionary.
    for continent, countrie_list in countries_dict.items():
        # Use a string method to format the required string.
        result += f"{countrie_list}\n"
    return result


print(
    countries(
        {
            "Africa": ["Kenya", "Egypt", "Nigeria"],
            "Asia": ["China", "India", "Thailand"],
            "South America": ["Ecuador", "Bolivia", "Brazil"],
        }
    )
)

# Should print:
# ['Kenya', 'Egypt', 'Nigeria']
# ['China', 'India', 'Thailand']
# ['Ecuador', 'Bolivia', 'Brazil']

##################################################################################################################

# Considere el siguiente escenario sobre el uso de diccionarios Python:

# Tessa y Rick organizan una fiesta.
# Juntos han enviado invitaciones y han recogido las respuestas en un diccionario,
# con los nombres de sus amigos y el número de invitados que llevará cada amigo.

# Complete la función para que la función "comprobar_invitados" recupere el número de invitados (valor)
# que el amigo "invitado" especificado (clave) va a traer.
# Esta función debería

# aceptar un diccionario "lista_invitados" y una variable clave "invitado" pasada a través de los parámetros de la función;

# imprimir los valores asociados a la variable clave.
def check_guests(guest_list, guest):
    """
    Devuelve el número de invitados que un amigo específico va a traer.

    Args:
        guest_list (dict): Un diccionario donde las claves son los nombres de los amigos y los valores son el número de invitados que traerán.
        guest (str): El nombre del amigo para comprobar su número de invitados.

    Returns:
        int: El número de invitados que el amigo especificado va a traer.
    """
    return guest_list[guest]  # Return the value for the given key


guest_list = {
    "Adam": 3,
    "Camila": 3,
    "David": 5,
    "Jamal": 3,
    "Charley": 2,
    "Titus": 1,
    "Raj": 6,
    "Noemi": 1,
    "Sakira": 3,
    "Chidi": 5,
}


print(check_guests(guest_list, "Adam"))  # Should print 3
print(check_guests(guest_list, "Sakira"))  # Should print 3
print(check_guests(guest_list, "Charley"))  # Should print 2

###################################################################################################################################

# Utilice un diccionario para contar la frecuencia de números en la cadena de "texto" dada.
# Sólo deben contarse los números.
# No cuente los espacios en blanco, las letras ni los signos de puntuación.
# Complete la función para que una entrada como "1001000111101" devuelva un diccionario que contenga el recuento de cada número que aparece en la cadena {'1': 7, '0': 6}.
# Esta función debería

# aceptar una variable de cadena "texto" a través de los parámetros de la función;

# inicializar un nuevo diccionario;

# iterar sobre cada carácter del texto para comprobar si el carácter es un número'

# contar la frecuencia de números en la cadena de entrada, ignorando todos los demás caracteres

# poblar el nuevo diccionario con los números como claves, asegurándose de que cada clave es única, y asignar al valor de cada clave el recuento de ese número;

# devuelva el nuevo diccionario.
def count_numbers(text):
    """
    Cuenta la frecuencia de cada número en una cadena.

    Args:
        text (str): La cadena para contar los números.

    Returns:
        dict: Un diccionario donde las claves son los números y los valores son sus frecuencias.
    """
    # Initialize a new dictionary.
    dictionary = {}
    # Complete the for loop to iterate through each "text" character.
    for n in text:
        # Complete the if-statement using a string method to check if the
        # character is a number.
        if n.isnumeric():
            # Complete the if-statement using a logical operator to check if
            # the number is not already in the dictionary.
            if n not in dictionary:
                # Use a dictionary operation to add the number as a key
                # and set the initial count value to zero.
                dictionary[n] = 0
            # Use a dictionary operation to increment the number count value
            # for the existing key.
            dictionary[n] += 1
    return dictionary


print(count_numbers("1001000111101"))
# Should be {'1': 7, '0': 6}

print(count_numbers("Math is fun! 2+2=4"))
# Should be {'2': 2, '4': 1}

print(count_numbers("This is a sentence."))
# Should be {}

print(count_numbers("55 North Center Drive"))
# Should be {'5': 2}

############################################################################################################################
