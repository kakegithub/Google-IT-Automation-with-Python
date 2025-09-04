# Ejemplos de comparaciones en Python con resultados esperados y explicaciones

print(10 > 1)  # True: 10 es mayor que 1

print("cat" == "dog")  # False: cadenas distintas

print(1 != 2)  # True: 1 es distinto de 2

# print(1 < "1")  # TypeError: no se pueden comparar int y str en Python 3

print(1 == "1")  # False: tipos distintos (int vs str) y valores no equivalentes

# Comparación lexicográfica (por orden Unicode) y operadores lógicos
# "Yellow" > "Cyan" -> True ("Y" > "C"); "Brown" > "Magenta" -> False ("B" < "M")
# True and False -> False
print("Yellow" > "Cyan" and "Brown" > "Magenta")  # False

# False or True -> True
print(25 > 50 or 1 != 2)  # True

# Es preferible usar != en lugar de "not a == b" por claridad
print(42 != "Answer")  # True: int y str nunca son iguales
