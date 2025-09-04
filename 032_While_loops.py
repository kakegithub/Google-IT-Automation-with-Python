# Bucles while: ejemplos y correcciones

# Ejemplo 1: incremento simple hasta alcanzar la condición de salida
x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x += 1
print("x=" + str(x))


# Ejemplo 2: función con while e incremento controlado

def attempts(n: int) -> None:
    """Imprime intentos desde 1 hasta n (inclusive)."""
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")


attempts(5)


# Ejemplo ilustrativo (comentado): dependencias no definidas provocarían NameError
# username = get_username()
# while not valid_username(username):
#     print("Invalid username")
#     username = get_username()
# Nota: get_username y valid_username no están definidas en este archivo.


# Otro ejemplo ilustrativo (comentado): NameError por variable no definida
# while my_variable < 10:
#     print("Hello")
#     my_variable += 1
# Solución: inicializar la variable antes del bucle.


# Versión correcta: variable inicializada antes de usarla en el bucle
my_variable = 5
while my_variable < 10:
    print("Hello")
    my_variable += 1


# Suma y producto con while
# Corrección: asegurar que x se restablece antes del segundo bucle y
# evitar sombrear la función incorporada 'sum' usando 'total'.

x = 1
total = 0
while x < 10:
    total += x
    x += 1

# Reiniciar x para calcular el producto correctamente desde 1
x = 1
product = 1
while x < 10:
    product *= x
    x += 1

print(total, product)
# Output corregido: 45 362880


# Múltiplos de 5 hasta 50
multiplier = 1
result = multiplier * 5
while result <= 50:
    print(result)
    multiplier += 1
    result = multiplier * 5
print("Done")

# Explicación:
# - Se imprime cada múltiplo de 5 aumentando 'multiplier' en 1 en cada iteración.
# - El bucle se detiene cuando 'result' supera 50.
