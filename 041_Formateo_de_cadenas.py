# Formateo de cadenas en Python: format(), marcadores con nombre y especificadores

# -----------------------------------------------------------------------------
# Ejemplo 1: placeholders posicionales con format()
name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))
# Salida: Hello Manny, your lucky number is 15

# -----------------------------------------------------------------------------
# Ejemplo 2: placeholders con nombre (más legible al reordenar o repetir)
name = "Manny"
print(
    "Your lucky number is {number}, {name}.".format(name=name, number=len(name) * 3)
)
# Salida: Your lucky number is 15, Manny.

# -----------------------------------------------------------------------------
# Ejemplo 3: formato numérico con especificadores (ancho y decimales)
price = 7.5
with_tax = price * 1.09
print(price, with_tax)  # valores crudos
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))
# Salida:
# 7.5 8.175
# Base price: $7.50. With Tax: $8.18

# -----------------------------------------------------------------------------
# Ejemplo 4: tabla con alineación y precisión

def to_celsius(x: float | int) -> float:
    """Convierte grados Fahrenheit a Celsius."""
    return (x - 32) * 5 / 9


for x in range(0, 101, 10):
    # {:>3} -> ancho 3, alineado a la derecha; {:>6.2f} -> ancho 6, 2 decimales
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

# -----------------------------------------------------------------------------
# Ejemplo 5: función que devuelve una cadena formateada

def student_grade(name: str, grade: int | float) -> str:
    """Retorna una frase con la nota del estudiante."""
    return "{} received {}% on the exam".format(name, grade)


print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))
