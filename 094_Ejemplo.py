import re


def check_character_groups(text):
    """
    Verifica si el texto contiene al menos dos grupos de caracteres de palabra
    (letras, números, guion bajo) separados por uno o más espacios.

    Args:
        text (str): La cadena de texto a verificar.

    Returns:
        bool: True si el patrón se encuentra, False en caso contrario.
    """
    # El patrón r"\w+\s+\w+" busca:
    # - \w+: uno o más caracteres de palabra.
    # - \s+: uno o más caracteres de espacio.
    # - \w+: uno o más caracteres de palabra.
    result = re.search(r"\w+\s+\w+", text)
    # Devuelve True si se encontró una coincidencia, False si no.
    return bool(result)


print(f"'One' -> {check_character_groups('One')}")  # False
# True
print(f"'123  Ready Set GO' -> {check_character_groups('123  Ready Set GO')}")
# True
print(f"'username user_01' -> {check_character_groups('username user_01')}")
# False
print(
    f"'shopping_list: milk, bread, eggs.' -> {check_character_groups('shopping_list: milk, bread, eggs.')}")
