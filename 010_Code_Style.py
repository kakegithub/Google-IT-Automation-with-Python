"""
Cálculo del área de un círculo: ejemplo con buenas prácticas de estilo.

Principios aplicados:
- Nombres descriptivos (circle_area, radius).
- Separación de responsabilidades: la función calcula y retorna; la impresión ocurre en main.
- Uso de math.pi en lugar de 3.14 para mayor precisión.
- Validación de entrada (tipo y no negatividad).
- Anotaciones de tipo y docstrings.
"""

import math
from numbers import Real


def circle_area(radius: Real) -> float:
    """
    Calcula el área de un círculo a partir de su radio.

    Fórmula: área = π * r^2.

    Parámetros:
        radius (Real): Radio del círculo. Debe ser numérico y no negativo.

    Retorna:
        float: Área del círculo.

    Excepciones:
        TypeError: Si 'radius' no es un número real.
        ValueError: Si 'radius' es negativo.
    """
    if not isinstance(radius, Real):
        raise TypeError("radius debe ser numérico (int o float).")
    if radius < 0:
        raise ValueError("radius debe ser no negativo.")

    return float(math.pi * (radius ** 2))


def main() -> None:
    # Ejemplo de uso: separar cálculo de presentación.
    r = 5
    area = circle_area(r)
    # Formateamos a 2 decimales para salida legible.
    print(f"El área del círculo de radio {r} es {area:.2f}")


if __name__ == "__main__":
    # Main guard: permite importar este módulo sin ejecutar efectos secundarios.
    main()


# Ejemplo de "mala práctica" (solo como referencia; NO ejecutar):
# - Nombres crípticos (calculate, d, q, z)
# - Número mágico 3.14 en lugar de math.pi
# - Mezcla de cálculo e impresión dentro de la función
# def calculate(d):
#     q = 3.14
#     z = q * (d ** 2)
#     print(z)
# calculate(5)
