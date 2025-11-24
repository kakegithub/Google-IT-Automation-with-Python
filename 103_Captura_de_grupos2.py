import re


def rearrange_name(name):
    # Modificamos el patrón para que acepte nombres con iniciales o segundos nombres.
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])


# Llama a la función e imprime el resultado para que sea visible.
print(rearrange_name("Ritchie, Dennis"))
