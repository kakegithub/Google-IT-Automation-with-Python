# Recursión: ejemplos de factorial, sumas y potencias

from __future__ import annotations


def factorial(n: int) -> int:
    """Retorna n! usando recursión.

    Caso base: n < 2 -> 1
    Caso recursivo: n * factorial(n-1)
    """
    if n < 2:
        return 1
    return n * factorial(n - 1)


def factorial_verbose(n: int) -> int:
    """Versión de factorial con trazas por pantalla para visualizar la recursión."""
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial_verbose(n - 1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result


# Ejemplo: traza de llamadas y luego resultado limpio
factorial_verbose(4)


def sum_positive_numbers(n: int) -> int:
    """Suma los enteros positivos desde n hasta 1 usando recursión.

    Caso base: n < 1 -> 0
    Caso recursivo: n + sum_positive_numbers(n-1)
    """
    if n < 1:
        return 0
    return n + sum_positive_numbers(n - 1)


print(sum_positive_numbers(3))  # Should be 6
print(sum_positive_numbers(5))  # Should be 15


def is_power_of(number: int, base: int) -> bool:
    """Determina si 'number' es una potencia entera de 'base'.

    Manejo de casos especiales para evitar recursión infinita:
    - Si number == 1 -> True (base**0)
    - Si base < 2 o number < 1 -> False (salvo el caso number == 1 anterior)

    En caso general, solo se divide si es exactamente divisible.
    """
    if number == 1:
        return True
    if base < 2 or number < 1:
        return False
    if number % base != 0:
        return False
    return is_power_of(number // base, base)


print(is_power_of(8, 2))   # Should be True
print(is_power_of(64, 4))  # Should be True
print(is_power_of(70, 10)) # Should be False


# Ejemplo comentado: contar usuarios con recursión sobre grupos anidados
# (Se dejan como comentarios para no depender de funciones externas no definidas.)
#
# def count_users(group):
#     count = 0
#     for member in get_members(group):
#         if is_group(member):
#             count += count_users(member)
#         else:
#             count += 1
#     return count
#
# print(count_users("sales"))        # Should be 3
# print(count_users("engineering"))  # Should be 8
# print(count_users("everyone"))     # Should be 18
