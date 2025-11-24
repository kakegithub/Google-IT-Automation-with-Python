import re


def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])


# Llama a la función e imprime el resultado para que sea visible.
print(rearrange_name("Hopper, Grace M."))
print(rearrange_name("Kennedy, John F."))
# Ejemplo que no coincide y devuelve el original.
print(rearrange_name("Voltaire"))
