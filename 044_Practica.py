# Práctica: cadenas, formateo y funciones utilitarias

# -----------------------------------------------------------------------------
# Ejemplo 1: cálculo de recibo a partir de una cesta de productos
# Cada ítem es una tupla (nombre, peso_en_libras, precio_por_libra)

basket = [("Peaches", 3.0, 2.99), ("Pears", 5.0, 1.66), ("Plums", 2.5, 3.99)]

# Subtotal acumulando peso * precio unitario
subtotal = 0.0
for item in basket:
    fruit, weight, unit_price = item
    subtotal += weight * unit_price

# Impuesto de ventas (New Jersey 6.625%) y total
tax_rate = 0.06625
tax_amt = subtotal * tax_rate
total = subtotal + tax_amt

# Impresión del recibo
print("Subtotal:", subtotal)
print("Sales Tax:", tax_amt)
print("Total:", total)

# -----------------------------------------------------------------------------
# Detección de cadena espejo (palíndromo ignorando caracteres no alfabéticos)

def mirrored_string(my_string: str) -> bool:
    """Devuelve True si my_string es palíndroma ignorando no letras (case-insensitive)."""
    forwards = ""
    backwards = ""
    for character in my_string:
        if character.isalpha():
            forwards += character
            backwards = character + backwards
    return forwards.lower() == backwards.lower()


print(mirrored_string("12 Noon"))                # True
print(mirrored_string("Was it a car or cat I saw"))  # False
print(mirrored_string("'eve, Madam Eve"))        # True

# -----------------------------------------------------------------------------
# Conversión de onzas a libras con 2 decimales

def convert_weight(ounces: float) -> str:
    """Convierte onzas a libras (1 lb = 16 oz) y formatea a 2 decimales."""
    pounds = ounces / 16
    return "{} ounces equals {:.2f} pounds".format(ounces, pounds)


print(convert_weight(12))    # 12 ounces equals 0.75 pounds
print(convert_weight(50.5))  # 50.5 ounces equals 3.16 pounds
print(convert_weight(16))    # 16 ounces equals 1.00 pounds

# -----------------------------------------------------------------------------
# Generación de nombre de usuario: 3 primeras letras del apellido + año nacimiento

def username(last_name: str, birth_year: str) -> str:
    """Genera un username a partir del apellido y el año de nacimiento."""
    return "{}{}".format(last_name[0:3], birth_year)


print(username("Ivanov", "1985"))      # Iva1985
print(username("Rodríguez", "2000"))   # Rod2000
print(username("Deng", "1991"))        # Den1991

# -----------------------------------------------------------------------------
# Reemplazar fecha al final de una frase si coincide exactamente

def replace_date(schedule: str, old_date: str, new_date: str) -> str:
    """Reemplaza old_date por new_date solo si aparece al final de schedule."""
    if schedule.endswith(old_date):
        p = len(old_date)
        new_schedule = schedule[:-p] + schedule[-p:].replace(old_date, new_date)
        return new_schedule
    return schedule


print(replace_date("Last year’s annual report will be released in March 2023", "2023", "2024"))
print(replace_date("In April, the CEO will hold a conference", "April", "May"))
print(replace_date("The convention is scheduled for October", "October", "June"))

# -----------------------------------------------------------------------------
# Comprobar si una cadena es palíndroma (ignora espacios y mayúsculas)

def is_palindrome(input_string: str) -> bool:
    """True si input_string es palíndroma ignorando espacios y puntuación; case-insensitive."""
    new_string = ""
    reverse_string = ""
    for letter in input_string:
        if letter.isalpha():  # Corrige: ignorar también puntuación, no solo espacios
            new_string = new_string + letter
            reverse_string = letter + reverse_string
    return new_string.upper() == reverse_string.upper()


print(is_palindrome("Never Odd or Even"))  # True
print(is_palindrome("abc"))                # False
print(is_palindrome("kayak"))              # True

# -----------------------------------------------------------------------------
# Conversión de distancia millas -> km (1 milla = 1.6 km)

def convert_distance(miles: float) -> str:
    """Convierte millas a km mostrando un decimal."""
    km = miles * 1.6
    return "{} miles equals {:.1f} km".format(miles, km)


print(convert_distance(12))   # 12 miles equals 19.2 km
print(convert_distance(5.5))  # 5.5 miles equals 8.8 km
print(convert_distance(11))   # 11 miles equals 17.6 km

# -----------------------------------------------------------------------------
# Etiqueta con inicial del apellido

def nametag(first_name: str, last_name: str) -> str:
    """Devuelve "Nombre A." usando la inicial del apellido."""
    return "{} {}.".format(first_name, last_name[0])


print(nametag("Jane", "Smith"))              # Jane S.
print(nametag("Francesco", "Rinaldi"))       # Francesco R.
print(nametag("Jean-Luc", "Grand-Pierre"))   # Jean-Luc G.

# -----------------------------------------------------------------------------
# Reemplazar final de cadena si coincide con 'old'

def replace_ending(sentence: str, old: str, new: str) -> str:
    """Reemplaza 'old' por 'new' solo si 'sentence' termina con 'old'."""
    if sentence.endswith(old):
        i = len(old)
        new_sentence = sentence[:-i] + sentence[-i:].replace(old, new)
        return new_sentence
    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
print(replace_ending("The weather is nice in May", "may", "april"))
print(replace_ending("The weather is nice in May", "May", "April"))
