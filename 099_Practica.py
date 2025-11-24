import re


def contains_acronym(text):
    """
    Verifica si el texto contiene un acrónimo entre paréntesis.

    Un acrónimo se define aquí como una palabra que comienza con una letra
    mayúscula o un número, seguida de letras o números, y encerrada
    entre paréntesis. Ejemplos: (IM), (ASCII), (4GL), (Scuba).

    Args:
        text (str): La cadena de texto a verificar.

    Returns:
        bool: True si se encuentra un acrónimo, False en caso contrario.
    """
    pattern = r"\([A-Z0-9][A-Za-z0-9]*\)"
    result = re.search(pattern, text)
    return bool(result)


print(contains_acronym(
    # True
    "Instant messaging (IM) is a set of communication technologies used for text-based communication"))
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication"))  # True
print(contains_acronym("Please do NOT enter without permission!"))  # False
print(contains_acronym(
    "PostScript is a fourth-generation programming language (4GL)"))  # True
print(contains_acronym(
    # True
    "Have fun using a self-contained underwater breathing apparatus (Scuba)!"))
