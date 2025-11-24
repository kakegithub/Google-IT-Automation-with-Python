import re


def check_zip_code(text):
    """
    Verifica si el texto contiene un código postal de EE. UU. válido (5 o 9 dígitos)
    que no se encuentre al principio de la cadena.

    Args:
        text (str): La cadena de texto a verificar.

    Returns:
        bool: True si se encuentra un código postal válido, False en caso contrario.
    """
    # \s: Busca un espacio antes del código.
    # \d{5}: Busca exactamente 5 dígitos.
    # (-\d{4})?: Opcionalmente, busca un guion seguido de 4 dígitos (formato ZIP+4).
    result = re.search(r"\s\d{5}(-\d{4})?", text)
    return bool(result)


# Call the check_zip_code function with test cases
print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code(
    "The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False
