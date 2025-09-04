# Operaciones con cadenas en Python: longitud, iteración, pertenencia, indexación y slicing

# Longitud de una cadena
print(len("abcde"))
# prints 5

# Iterar sobre cada carácter de la cadena
for c in "abcde":
    print(c)
# prints "a", then "b", then "c", etc.

# Comprobar si una subcadena forma parte de la cadena (operador 'in')
print("abc" in "abcde")  # prints True
print("def" in "abcde")  # prints False

# Acceso por índice (empezando en 0) y por índice negativo (desde el final)
print("abcde"[2])   # prints "c"
print("abcde"[-1])  # prints "e"

# Rebanado (slicing): [inicio:fin] y desde un índice hasta el final
print("abcde"[0:2])  # prints "ab"
print("abcde"[2:])   # prints "cde"
