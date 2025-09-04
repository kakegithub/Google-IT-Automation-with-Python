# Práctica: bucles for/while, rangos y construcción de cadenas

# -----------------------------------------------------------------------------
# Uso de bucles for con la función range()

def count_by_10(end: int) -> str:
    """Cuenta de 10 en 10 desde 0 hasta end (inclusive) y retorna una cadena."""
    # " ".join(...) evita espacios sobrantes y es eficiente
    return " ".join(str(n) for n in range(0, end + 1, 10))


# Llamada de ejemplo
print(count_by_10(100))
# Debe imprimir: 0 10 20 30 40 50 60 70 80 90 100

# -----------------------------------------------------------------------------
# Matriz con bucles anidados y range()

def matrix(initial_number: int, end_of_first_row: int) -> None:
    """Imprime una matriz de productos desde initial_number hasta end_of_first_row.

    Ambos límites son inclusivos.
    """
    start = initial_number
    end = end_of_first_row + 1  # incluir el límite superior

    for column in range(start, end):  # columnas
        for row in range(start, end):  # filas
            print(column * row, end=" ")
        print()  # nueva línea al terminar cada fila


# Llamada de ejemplo
matrix(1, 4)
# Debe imprimir:
# 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16

# -----------------------------------------------------------------------------
# Predecir el valor final de un bucle for anidado con range()
# Bucle externo: range(10) -> 0..9
# Bucle interno: range(outer_loop) -> 0..outer_loop-1
for outer_loop in range(10):
    for inner_loop in range(outer_loop):
        print(inner_loop)

# -----------------------------------------------------------------------------
# Contar hacia atrás de 11 a 1, solo impares (paso -2 correcto)
for n in range(11, 0, -2):
    if n % 2 != 0:
        print(n, end=" ")
print()
# Debe imprimir: 11 9 7 5 3 1

# -----------------------------------------------------------------------------
# Utilizar un bucle while para imprimir una secuencia de números
# Cuenta regresiva de 18 a 0 en pasos de 3
starting_number = 18
while starting_number >= 0:
    print(starting_number, end=" ")
    starting_number -= 3
print()
# Debe imprimir: 18 15 12 9 6 3 0

# -----------------------------------------------------------------------------
# Contar el número de d��gitos de un salario

def X_figure(salary: int) -> int:
    """Cuenta los dígitos de salary. 0 tiene 1 dígito por convención."""
    if salary == 0:
        return 1
    tally = 0
    while salary > 0:
        salary //= 10  # división entera para evitar flotantes
        tally += 1
    return tally


print("The CEO has a " + str(X_figure(2_300_000)) + "-figure salary.")
# Debe imprimir: The CEO has a 7-figure salary.

# -----------------------------------------------------------------------------
# Conteo de pisos en un ascensor (subiendo o bajando)

def elevator_floor(enter: int, exit: int) -> str:
    """Devuelve la secuencia de pisos entre enter y exit, con dirección."""
    if enter > exit:
        direction = "Going down: "
        floors = range(enter, exit - 1, -1)  # inclusivo hacia abajo
    else:
        direction = "Going up: "
        floors = range(enter, exit + 1)  # inclusivo hacia arriba

    return direction + " | ".join(str(f) for f in floors)


print(elevator_floor(1, 4))  # Debe imprimir: Going up: 1 | 2 | 3 | 4
print(elevator_floor(6, 2))  # Debe imprimir: Going down: 6 | 5 | 4 | 3 | 2
