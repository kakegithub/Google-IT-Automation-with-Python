import re


def check_aei(text):
    """
    Verifica si el texto contiene las vocales 'a', 'e', 'i' en ese orden,
    separadas por un único carácter entre ellas (ej: aXeXi).

    Args:
        text (str): La cadena de texto a verificar.

    Returns:
        bool: True si el patrón se encuentra, False en caso contrario.
    """
    # El patrón r"a.e.i" busca una 'a', seguida de cualquier carácter (.),
    # luego una 'e', seguida de cualquier carácter (.), y finalmente una 'i'.
    result = re.search(r"a.e.i", text)
    # Es más idiomático en Python devolver el resultado booleano del objeto match.
    # El objeto es "truthy" (verdadero) si hay coincidencia, y "falsy" (falso) si es None.
    return bool(result)


# True (coincide con 'ademi')
print(f"'academia' contiene el patrón 'a.e.i': {check_aei('academia')}")
# False (no hay carácter entre 'e' e 'i')
print(f"'aerial' contiene el patrón 'a.e.i': {check_aei('aerial')}")
# True (coincide con 'amedi')
print(f"'paramedic' contiene el patrón 'a.e.i': {check_aei('paramedic')}")
