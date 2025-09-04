"""
Calcula el número total de días a partir de años, meses y días.
Suposición: 1 mes = 30 días. No contempla años bisiestos.
"""


def find_total_days(years: int, months: int, days: int) -> int:
    """
    Calcula el total de días dado un número de años, meses y días.

    Parámetros:
        years (int): Cantidad de años.
        months (int): Cantidad de meses (se asume 30 días por mes).
        days (int): Cantidad de días.

    Retorna:
        int: Total de días.
    """
    # Convertir años y meses a días y sumarlos con los días recibidos
    total_days = years * 365 + months * 30 + days
    return total_days


if __name__ == "__main__":
    # Ejemplo de uso: 2 años, 5 meses y 23 días
    print(find_total_days(2, 5, 23))
