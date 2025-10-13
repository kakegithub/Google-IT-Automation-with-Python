import re


def repeating_letter_a(text):
    """
    Verifica si la letra 'a' (mayúscula o minúscula) aparece al menos
    dos veces en el texto.

    Args:
        text (str): La cadena de texto a verificar.

    Returns:
        bool: True si la letra 'a' se repite, False en caso contrario.
    """
    # El patrón r"a.*a" busca:
    # - 'a': la primera letra 'a'.
    # - '.*': cualquier carácter (.), cero o más veces (*).
    # - 'a': la segunda letra 'a'.
    # re.IGNORECASE hace que la búsqueda no distinga entre 'a' y 'A'.
    result = re.search(r"a.*a", text, re.IGNORECASE)

    # Devuelve True si se encontró una coincidencia, False si no.
    return bool(result)


# True
print(f"'banana' contiene al menos dos 'a': {repeating_letter_a('banana')}")
# False
print(
    f"'pineapple' contiene al menos dos 'a': {repeating_letter_a('pineapple')}")
# True
print(
    f"'Animal Kingdom' contiene al menos dos 'a': {repeating_letter_a('Animal Kingdom')}")
# True
print(
    f"'A is for apple' contiene al menos dos 'a': {repeating_letter_a('A is for apple')}")
