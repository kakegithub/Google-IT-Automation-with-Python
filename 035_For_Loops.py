# Bucles for: ejemplos de iteración sobre rangos, listas y acumuladores

# -----------------------------------------------------------------------------
# Ejemplo 1: iterar un rango 0..4 (5 elementos)
for x in range(5):
    print(x)

# -----------------------------------------------------------------------------
# Ejemplo 2: iterar sobre una lista de cadenas
friends = ["Taylor", "Alex", "Pat", "Eli"]
for friend in friends:
    print("Hi " + friend)

# -----------------------------------------------------------------------------
# Ejemplo 3: suma y promedio de una lista de valores
values = [23, 52, 59, 37, 48]
# Evitar sombrear la función incorporada sum() usando nombres distintos
total = 0
count = 0
for value in values:
    total += value
    count += 1

print("Total sum: " + str(total) + " - Average: " + str(total / count))

# -----------------------------------------------------------------------------
# Ejemplo 4: producto acumulado (factorial de 1..9)
product = 1
for n in range(1, 10):
    product *= n
print(product)  # 362880

# -----------------------------------------------------------------------------
# Ejemplo 5: conversión de Fahrenheit a Celsius cada 10°F

def to_celsius(f: float | int) -> float:
    """Convierte grados Fahrenheit a Celsius."""
    return (f - 32) * 5 / 9


for f in range(0, 101, 10):
    print(f, to_celsius(f))

# -----------------------------------------------------------------------------
# Ejemplo 6: uso del parámetro step (salto) en range
# Comienza en 1, incrementa de 6 en 6, se detiene antes de 20 -> 1, 7, 13, 19
for n in range(1, 20, 6):
    print(n)

# -----------------------------------------------------------------------------
# Ejemplo 7: imprimir números pares de 0 a 10 usando step=2
# range(0, 11, 2) genera 0, 2, 4, 6, 8, 10
for n in range(0, 11, 2):
    print(n)

# -----------------------------------------------------------------------------
# Ejemplo 8: multiplicar números de 2 a 7 por 3 (incluye 7)
for number in range(2, 7 + 1):
    print(number * 3)

# -----------------------------------------------------------------------------
# Ejemplo 9: cuenta regresiva desde 2 hasta -1 con paso -1
for x in range(2, -2, -1):
    print(x)
