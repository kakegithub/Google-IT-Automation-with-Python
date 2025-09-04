# Listas en Python: creación, acceso, pertenencia y slicing

# -----------------------------------------------------------------------------
# Creación de una lista y operaciones básicas
x = ["Now", "we", "are", "cooking!"]

# Tipo de dato y contenido de la lista
print(type(x))                 # <class 'list'>
print(x)                       # ['Now', 'we', 'are', 'cooking!']

# Longitud de la lista
print(len(x))                  # 4

# Operador de pertenencia 'in'
print("are" in x)             # True
print("Today" in x)           # False

# Indexación (comienza en 0)
print(x[0])                    # "Now"
print(x[3])                    # "cooking!"
# print(x[4])                 # IndexError: índice fuera de rango

# Slicing (rebanado)
print(x[1:3])                  # ['we', 'are']
print(x[:2])                   # ['Now', 'we']
print(x[2:])                   # ['are', 'cooking!']

# -----------------------------------------------------------------------------
# Función: obtener la n‑ésima palabra (1-based) de una oración

def get_word(sentence: str, n: int) -> str:
    """Devuelve la n‑ésima palabra (base 1) de 'sentence'.

    - Si n <= 0 o n es mayor que el número de palabras, retorna "".
    - Las palabras se separan por espacios en blanco (split()).
    """
    if n > 0:
        words = sentence.split()
        if n <= len(words):
            # Índice 1-based -> 0-based
            return words[n - 1]
    return ""


# Pruebas de la función
print(get_word("This is a lesson about lists", 4))   # Debe imprimir: lesson
print(get_word("This is a lesson about lists", -4))  # No debe imprimir nada -> ""
print(get_word("Now we are cooking!", 1))            # Debe imprimir: Now
print(get_word("Now we are cooking!", 5))            # No debe imprimir nada -> ""
