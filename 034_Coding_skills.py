# Habilidades: conteo de factores y tabla de suma con bucles while


def count_factors(given_number: int) -> int:
    """Cuenta la cantidad de factores enteros positivos de given_number.

    Nota:
    - Por convenio en este ejemplo, si given_number es 0 se retorna 0,
      aunque matemáticamente el 0 tiene infinitos divisores.
    - El algoritmo incluye a given_number como factor (n * 1).
    """
    # Caso especial: 0
    if given_number == 0:
        return 0

    # Inicializamos el divisor en 1 e iniciamos el conteo en 1 para contar al propio número
    divisor = 1
    num_factors = 1  # Contabiliza 'given_number' como factor

    # Recorremos divisores estrictamente menores que el número
    while divisor < given_number:
        # Si divide exactamente (sin resto), es un factor válido
        if given_number % divisor == 0:
            num_factors += 1
        # Siguiente posible divisor
        divisor += 1

    return num_factors


print(count_factors(0))   # Count value should be 0
print(count_factors(3))   # Should count 2 factors (1x3)
print(count_factors(10))  # Should count 4 factors (1x10, 2x5)
print(count_factors(24))  # Should count 8 factors (1x24, 2x12, 3x8, and 4x6)


# -----------------------------------------------------------------------------
# Esta función imprime una tabla de sumas. Está escrita para terminar tras
# imprimir 5 líneas, pero saldrá antes si la suma excede 20.


def addition_table(given_number: int) -> None:
    """Imprime hasta 5 líneas de la tabla de suma del número dado.

    Se detiene si given_number + iterated_number > 20.
    Retorna None implícitamente (no hay return explícito).
    """
    iterated_number = 1

    # Itera mientras el contador sea menor o igual a 5
    while iterated_number <= 5:
        my_sum = given_number + iterated_number

        # Si la suma excede 20, se interrumpe el bucle
        if my_sum > 20:
            break

        # Muestra la operación y el resultado
        print(f"{given_number} + {iterated_number} = {my_sum}")

        # Incrementa para la siguiente línea
        iterated_number += 1


addition_table(5)
addition_table(17)
addition_table(30)

# Salida esperada:
# 5 + 1 = 6
# 5 + 2 = 7
# 5 + 3 = 8
# 5 + 4 = 9
# 5 + 5 = 10
# 17 + 1 = 18
# 17 + 2 = 19
# 17 + 3 = 20
# (La función retorna None implícitamente; no imprime una línea adicional)
