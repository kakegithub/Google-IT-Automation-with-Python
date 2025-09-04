# 1) La función imprime el total de segundos a partir de horas, minutos y segundos
def print_seconds(hours: int, minutes: int, seconds: int) -> None:
    """Imprime el total de segundos a partir de horas, minutos y segundos.

    Parámetros:
        hours (int): Cantidad de horas.
        minutes (int): Cantidad de minutos.
        seconds (int): Cantidad de segundos.
    """
    total_seconds = hours * 3600 + minutes * 60 + seconds  # 1 h = 3600 s; 1 min = 60 s
    print(total_seconds)

# 2) Ejemplo de uso: imprimirá el resultado en pantalla
print_seconds(1, 2, 3)
