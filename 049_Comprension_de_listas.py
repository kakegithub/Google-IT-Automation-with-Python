# Ejemplo 1: Crear una lista de múltiplos de 7 usando un bucle for
multiples = []
for x in range(1, 11):
    multiples.append(x * 7)

print(multiples)
# Resultado: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

# Ejemplo 2: Crear la misma lista de múltiplos de 7 usando comprensión de listas
multiples = [x * 7 for x in range(1, 11)]
print(multiples)
# Resultado: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

# Ejemplo 3: Crear una lista con la longitud de cada string en la lista de lenguajes
languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)
# Resultado: [6, 4, 4, 2, 4, 1]

# Ejemplo 4: Crear una lista de números divisibles por 3 en el rango de 0 a 100 usando comprensión de listas
z = [x for x in range(0, 101) if x % 3 == 0]
print(z)
# Resultado: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
