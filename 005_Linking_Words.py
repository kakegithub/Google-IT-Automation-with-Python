"""
Ejemplo de construcción de un nombre completo usando concatenación de cadenas
("+") y usando múltiples argumentos en print separados por comas.

- Con el operador + se concatenan cadenas tal cual, por lo que hay que incluir
  manualmente espacios y signos de puntuación en las cadenas.
- Con print(a, b, c, ...) Python inserta un espacio entre cada argumento
  automáticamente. Si uno de los argumentos es "," (coma) como cadena, quedará
  un espacio antes y después de esa coma.
"""

# Asignación de componentes del nombre a variables de tipo str
salutation = "Dr."
first_name = "Prisha"
middle_name = "Jai"
last_name = "Agarwal"
suffix = "Ph.D."

# Concatenación explícita con +
# - Se añaden espacios como literales " " entre los componentes
# - Se añade ", " para la convención de coma + espacio antes del sufijo
print(
    salutation
    + " "
    + first_name
    + " "
    + middle_name
    + " "
    + last_name
    + ", "
    + suffix
)

# Alternativa: usar múltiples argumentos en print, separados por comas.
# print inserta espacios entre argumentos automáticamente. Aquí pasamos ","
# como un argumento más, por lo que la salida tendrá un espacio antes y después
# de la coma (p. ej., "Agarwal , Ph.D.").
print(salutation, first_name, middle_name, last_name, ",", suffix)
