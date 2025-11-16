import re


def check_sentence(text):
    """
    Verifica si el texto se parece a una oración estándar:
    - Empieza con una letra mayúscula.
    - Es seguida por letras minúsculas, espacios y algunos signos de puntuación.
    - Termina con un punto, signo de interrogación o exclamación.
    """
    # ^[A-Z]      : Empieza con una letra mayúscula.
    # [a-z\s,'.]* : Seguido de cero o más letras minúsculas, espacios, comas, etc.
    # [.?!]$      : Termina con un punto, '?' o '!'.
    result = re.search(r"^[A-Z][a-z\s,'.]*[.?!]$", text)
    return bool(result)


# True
print(
    f"'Is this is a sentence?' -> {check_sentence('Is this is a sentence?')}")
# False (no empieza con mayúscula)
print(
    f"'is this is a sentence?' -> {check_sentence('is this is a sentence?')}")
# False (no termina con puntuación)
print(f"'Hello' -> {check_sentence('Hello')}")
# False (no empieza con letra mayúscula)
print(f"'1-2-3-GO!' -> {check_sentence('1-2-3-GO!')}")
print(f"'A star is born.' -> {check_sentence('A star is born.')}")  # True
# True (maneja comas y apóstrofos)
print(f"'She said, 'hello'.' -> {check_sentence('She said, \'hello\'.')}")
# False (no termina con la puntuación correcta)
print(f"'Ends with a comma,' -> {check_sentence('Ends with a comma,')}")
