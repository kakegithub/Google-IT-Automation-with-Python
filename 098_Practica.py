import re


def check_time(text):
    """
    Valida si una cadena de texto tiene un formato de hora de 12 horas válido.

    Un formato válido debe:
    - Empezar con una hora de 1 a 12.
    - Seguir con dos puntos ':'.
    - Continuar con minutos de 00 a 59.
    - Terminar con 'am' o 'pm' (case-insensitive), precedido opcionalmente por un espacio.

    Args:
        text (str): La cadena a validar.

    Returns:
        bool: True si el formato es válido, False en caso contrario.
    """
    pattern = r"^(1[0-2]|[1-9]):[0-5][0-9] ?([ap]m)$"
    # Añadimos re.IGNORECASE para que el patrón no distinga entre mayúsculas y
    # minúsculas, validando así "am", "AM", "pm", "PM", etc.
    result = re.search(pattern, text, re.IGNORECASE)
    return bool(result)


print(check_time("12:45pm"))  # True
print(check_time("9:59 AM"))  # True
print(check_time("6:60am"))  # False
print(check_time("five o'clock"))  # False
print(check_time("6:02 am"))  # True
print(check_time("6:02km"))  # False
