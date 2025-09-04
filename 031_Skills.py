# Habilidades: condicionales, mapeos y valores absolutos


def clothing_type(temp: float | int) -> str:
    """Devuelve el tipo de prenda sugerida según la temperatura.

    Reglas (incluye/excluye límites para replicar el comportamiento original):
        - temp <= 32 -> "Heavy Coat"
        - 32 < temp <= 50 -> "Jacket"
        - 50 < temp <= 65 -> "Sweatshirt"
        - temp > 65 -> "T-Shirt"
    """
    if temp <= 32:
        return "Heavy Coat"
    elif temp <= 50:
        return "Jacket"
    elif temp <= 65:
        return "Sweatshirt"
    else:
        return "T-Shirt"


print(clothing_type(72))  # Should print T-Shirt
print(clothing_type(55))  # Should print Sweatshirt
print(clothing_type(65))  # Should print Sweatshirt
print(clothing_type(50))  # Should print Jacket
print(clothing_type(45))  # Should print Jacket
print(clothing_type(32))  # Should print Heavy Coat
print(clothing_type(0))   # Should print Heavy Coat

# -----------------------------------------------------------------------------


def letter_translator(letter: str) -> int | str:
    """Traduce letras 'a'..'d' a su posición (1..4); otros casos -> "unknown".

    La comparación es sensible a mayúsculas/minúsculas ("A" -> "unknown").
    """
    mapping = {"a": 1, "b": 2, "c": 3, "d": 4}
    return mapping.get(letter, "unknown")


print(letter_translator("a"))  # Should print 1
print(letter_translator("b"))  # Should print 2
print(letter_translator("c"))  # Should print 3
print(letter_translator("d"))  # Should print 4
print(letter_translator("e"))  # Should print unknown
print(letter_translator("A"))  # Should print unknown
print(letter_translator(""))   # Should print unknown

# -----------------------------------------------------------------------------


def make_positive(number: float | int) -> float | int:
    """Devuelve el valor absoluto del número (positivo o cero)."""
    return abs(number)


print(make_positive(-4))     # Should print 4
print(make_positive(0))      # Should print 0
print(make_positive(-0.25))  # Should print 0.25
print(make_positive(5))      # Should print 5
