# Cadenas en Python: inmutabilidad, búsqueda, transformación y utilidades

# -----------------------------------------------------------------------------
# Inmutabilidad: no se puede asignar a un índice de una cadena
# Forma incorrecta (lanza error):
# message = "A kong string with a silly typo"
# message[2] = "l"
# Forma correcta: reconstruir con slicing + concatenación
message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]
print(new_message)  # "A long string with a silly typo"

# -----------------------------------------------------------------------------
# Reasignación: las variables pueden apuntar a nuevas cadenas
message = "This is a new message"
print(message)
message = "And another one"
print(message)

# -----------------------------------------------------------------------------
# Búsqueda de subcadenas: index vs find
pets = "Cats & Dogs"

# index lanza ValueError si no encuentra; se muestra con try/except
try:
    print("Index de '&':", pets.index("&"))
    print("Index de 'C':", pets.index("C"))
    # Esta línea lanzaría error si se busca 'Dog' exacto (sin 's'); usamos find como alternativa
    print("Index de 'Dog' con find (seguro):", pets.find("Dog"))  # -1 si no está
    print("Index de 's':", pets.index("s"))  # primer 's'
except ValueError as e:
    print("Búsqueda con index falló:", e)

# Ejemplo de búsqueda fallida con index (comentado para evitar excepción)
# pets.index("x")  # ValueError

# Operador de pertenencia 'in'
print("Dragons" in pets)  # False
print("Cats" in pets)     # True

# -----------------------------------------------------------------------------
# Reemplazo de dominio en emails

def replace_domain(email: str, old_domain: str, new_domain: str) -> str:
    """Reemplaza el dominio de un email si coincide con old_domain.

    Ejemplo: replace_domain("user@old.com", "old.com", "new.com") -> "user@new.com"
    """
    token = "@" + old_domain
    if token in email:
        index = email.index(token)
        return email[:index] + "@" + new_domain
    return email


print(replace_domain("alice@example.com", "example.com", "new.org"))
print(replace_domain("bob@other.org", "example.com", "new.org"))

# -----------------------------------------------------------------------------
# Otros ejemplos de búsqueda
animals = "lions tigers and bears"
print("Index de 'g' con find:", animals.find("g"))      # 8
print("Index de 'bears' con index:", animals.index("bears"))  # 17

# -----------------------------------------------------------------------------
# Mayúsculas/minúsculas
print("Mountains".upper())
print("Mountains".lower())

answer = "YES"
if answer.lower() == "yes":
    print("User said yes")

# -----------------------------------------------------------------------------
# Espacios en blanco a izquierda/derecha
print("_" + " yes ".strip() + "_")   # ambos lados
print("_" + " yes ".lstrip() + "_")  # izquierda
print("_" + " yes ".rstrip() + "_")  # derecha

# -----------------------------------------------------------------------------
# Contar apariciones de subcadena
print("The number of times e occurs in this string is 4".count("e"))

# -----------------------------------------------------------------------------
# Sufijos y contenido numérico
print("Forest".endswith("rest"))
print("Forest".isnumeric())
print("12345".isnumeric())

# Conversión a entero y suma
print(int("12345") + int("54321"))

# -----------------------------------------------------------------------------
# Unir (join) y separar (split)
print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))
print("...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"]))
print("This is another example".split())
