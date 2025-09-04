# Operador lógico 'and': el resultado es True solo si ambas condiciones son True

# Ejemplo 1
# 6*3 = 18 -> 18 >= 18 => True
# 9+9 = 18 y 36/2 = 18.0 -> 18 <= 18.0 => True
# True and True -> True
print((6 * 3 >= 18) and (9 + 9 <= 36 / 2))

# Ejemplo 2
# Comparación lexicográfica de cadenas (Unicode):
# "Nairobi" < "Milan" -> False ('N' > 'M')
# "Nairobi" > "Hanoi" -> True ('N' > 'H')
# False and True -> False
print("Nairobi" < "Milan" and "Nairobi" > "Hanoi")
