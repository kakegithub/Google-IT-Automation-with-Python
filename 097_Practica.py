import re


def check_web_address(text):
    """
    Valida si una cadena de texto tiene el formato de una dirección web simple.

    Una dirección válida debe:
    - Contener solo letras, números, guiones, guiones bajos y puntos.
    - Terminar con un punto seguido de letras (el dominio de nivel superior).
    - Coincidir con la cadena completa, sin caracteres extra.

    Args:
        text (str): La cadena a validar.

    Returns:
        bool: True si la cadena es una dirección web válida, False en caso contrario.
    """
    pattern = r"^[\w\.-]+\.[a-zA-Z]+$"
    result = re.search(pattern, text)
    return bool(result)


print(check_web_address("gmail.com"))  # True
print(check_web_address("www@google"))  # False
print(check_web_address("www.Coursera.org"))  # True
print(check_web_address("web-address.com/homepage"))  # False
print(check_web_address("My_Favorite-Blog.US"))  # True
