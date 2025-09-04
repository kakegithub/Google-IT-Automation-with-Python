# Validación de nombre de usuario mediante ramificación con if/elif/else

def hint_username(username: str) -> None:
    """Imprime sugerencias de validación para un nombre de usuario.

    Reglas:
    - Debe tener al menos 3 caracteres.
    - Debe tener como máximo 15 caracteres.

    Parámetros:
        username (str): Nombre de usuario a validar.
    """
    if len(username) < 3:
        # Caso: demasiado corto
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        # Caso: demasiado largo
        print("Invalid username. Must be at most 15 characters long")
    else:
        # Caso: longitud válida
        print("Valid username")


# Ejemplos de uso (descomenta para probar):
# hint_username("ab")         # -> Invalid username. Must be at least 3 characters long
# hint_username("usuario_ok") # -> Valid username
# hint_username("x" * 16)     # -> Invalid username. Must be at most 15 characters long
