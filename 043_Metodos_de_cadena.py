# Métodos de cadena en Python: ejemplos comentados

# -----------------------------------------------------------------------------
# string.lower() -> copia en minúsculas
print("AaBbCcDdEe".lower())  # aabbccddee

# -----------------------------------------------------------------------------
# string.upper() -> copia en mayúsculas
print("AaBbCcDdEe".upper())  # AABBCCDDEE

# -----------------------------------------------------------------------------
# string.lstrip() / rstrip() / strip() -> recorte de espacios en blanco
print("  Hello  ".lstrip())  # "Hello  " (recorta a la izquierda)
print("  Hello  ".rstrip())  # "  Hello" (recorta a la derecha)
print("   Hello   ".strip())  # "Hello" (recorta ambos lados)

# -----------------------------------------------------------------------------
# string.count(substring) -> número de apariciones
text_spaces = "How much wood would a woodchuck chuck"
print(text_spaces.count("wood"))  # 2

# -----------------------------------------------------------------------------
# string.isnumeric() -> True si todos los caracteres son numéricos
print("12345".isnumeric())   # True
print("-123.45".isnumeric())  # False

# -----------------------------------------------------------------------------
# string.isalpha() -> True si todos los caracteres son letras
print("xyzzy".isalpha())  # True

# -----------------------------------------------------------------------------
# string.split() -> lista de palabras separadas por espacio
print(text_spaces.split())
# ['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck']

# -----------------------------------------------------------------------------
# string.split(delimiter) -> lista separada por un delimitador concreto
text_hyphen = "How-much-wood-would-a-woodchuck-chuck"
print(text_hyphen.split("-"))
# ['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck']

# -----------------------------------------------------------------------------
# string.replace(old, new) -> reemplaza todas las apariciones
print(text_spaces.replace("wood", "plastic"))
# "How much plastic would a plasticchuck chuck"

# -----------------------------------------------------------------------------
# delimiter.join(lista) -> une cadenas con un delimitador
print("-".join(text_spaces.split()))
# "How-much-wood-would-a-woodchuck-chuck"
