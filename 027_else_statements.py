# Ejemplos de uso de else y elif con buenas prácticas de estilo

# Ejemplo 1: if/else básico

def hint_username_simple(username: str) -> None:
    """Imprime si un nombre de usuario es válido con la regla mínima de longitud.

    Regla:
        - Debe tener al menos 3 caracteres.
    """
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        print("Valid username")


username = "Clarice"
hint_username_simple(username)
print()

# Ejemplo 2: función que devuelve un booleano usando else implícito

def is_even(number: int) -> bool:
    """Devuelve True si number es par, False en caso contrario."""
    return number % 2 == 0


number = 9
print(is_even(number))
print()

# Ejemplo 3a: if/else anidados para múltiples condiciones

def hint_username_nested(username: str) -> None:
    """Valida nombre de usuario con reglas de longitud usando if/else anidado.

    Reglas:
        - Longitud mínima: 3
        - Longitud máxima: 15
    """
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        if len(username) > 15:
            print("Invalid username. Must be at most 15 characters long")
    
        else:
            print("Valid username")


username = "blackman"
hint_username_nested(username)
print()

# Ejemplo 3b: versión equivalente usando elif (más clara)

def hint_username_elif(username: str) -> None:
    """Valida nombre de usuario con elif para mayor claridad."""
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valid username")


username = "Jordan"
hint_username_elif(username)
print()
