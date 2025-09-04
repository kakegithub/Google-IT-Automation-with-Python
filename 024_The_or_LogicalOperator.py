# Operador lógico 'or': el resultado es True si al menos UNA condición es True

# Variables de ejemplo
country = "United States"
city = "New York City"

# True or True -> True
# 15/3 = 5.0 y 2+4 = 6  =>  5.0 < 6  => True
# 0 >= 6-7  =>  0 >= -1  => True
print((15 / 3 < 2 + 4) or (0 >= 6 - 7))  # True

# False or True -> True
# country == "New York City"  =>  "United States" == "New York City"  => False
# city == "New York City"  =>  True
print(country == "New York City" or city == "New York City")  # True

# True or False -> True
# 16 <= 4**2  =>  16 <= 16  => True
# 9**0.5 != 3  =>  3.0 != 3  => False (3.0 y 3 son equivalentes en igualdad)
print(16 <= 4 ** 2 or 9 ** 0.5 != 3)  # True

# False or False -> False (comparación lexicográfica por Unicode)
# "B_name" > "C_name"  =>  False ('B' < 'C')
# "B_name" < "A_name"  =>  False ('B' > 'A')
print("B_name" > "C_name" or "B_name" < "A_name")  # False
