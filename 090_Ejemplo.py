"""
Este script comprueba si una cadena de texto contiene alguno de los siguientes
signos de puntuación: coma, punto, dos puntos, punto y coma, signo de
interrogación o signo de exclamación.
"""
import re


def check_punctuation(text):
    """
    Verifica si el texto contiene algún signo de puntuación común.

    Args:
        text (str): La cadena de texto a verificar.

    Returns:
        bool: True si se encuentra un signo de puntuación, False en caso contrario.
    """
    # El patrón r"[,.:;?!]" busca cualquier carácter que esté dentro de los corchetes.
    # Es una "clase de caracteres".
    result = re.search(r"[,.:;?!]", text)
    # Devuelve True si se encontró una coincidencia (el resultado no es None),
    # y False en caso contrario.
    return bool(result)


# True
print(
    f"'This is a sentence that ends with a period.' -> {check_punctuation('This is a sentence that ends with a period.')}")
# False
print(
    f"'This is a sentence fragment without a period' -> {check_punctuation('This is a sentence fragment without a period')}")
# True
print(
    f"'Aren't regular expressions awesome?' -> {check_punctuation('Aren\'t regular expressions awesome?')}")
# True
print(
    f"'Wow! We're really picking up some steam now!' -> {check_punctuation('Wow! We\'re really picking up some steam now!')}")
print(f"'End of the line' -> {check_punctuation('End of the line')}")  # False
