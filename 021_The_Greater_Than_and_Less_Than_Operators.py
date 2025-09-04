# Operadores mayor que (>) y menor que (<) con cadenas: comparación lexicográfica (Unicode)

print("Wednesday" > "Friday")  # True: 'W'(87) > 'F'(70)

# Las minúsculas tienen mayor valor Unicode que las mayúsculas
print("Brown" < "brown")  # True: 'B'(66) < 'b'(98)

# Se comparan letra a letra hasta encontrar una diferencia
print("sunbathe" > "suntan")  # False: 'b'(98) < 't'(116) en la 4ª letra

# Cadenas idénticas no son ni < ni > (son iguales)
print("Lima" < "Lima")  # False

# No se pueden comparar tipos distintos con < o >; produce TypeError
# print("Five" < 6)  # TypeError: '<' no está soportado entre 'str' e 'int'
