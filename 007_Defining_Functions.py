"""
Demostración de:
- Definición de funciones en Python (con parámetro opcional)
- Uso de funciones incorporadas: print, type, str, sorted, min, max

Corrección aplicada:
Antes había dos funciones llamadas 'greeting' con distinta firma. En Python la
segunda definición sobrescribe a la primera (no existe sobrecarga por firma),
lo que puede causar confusión. Se unifica en una sola función con un parámetro
opcional 'department' para permitir ambos usos con una única definición.
"""


def greeting(name, department=None):
    """Saluda a la persona y, opcionalmente, indica su departamento.

    Args:
        name (str): Nombre de la persona a saludar.
        department (str | None): Nombre del departamento (opcional).
    """
    print("Welcome, " + name)
    if department is not None:
        print("You are part of " + department)


# Llamadas de ejemplo a la función greeting
# - Sin departamento (solo un saludo)
greeting("Kay")
greeting("Cameron")

# - Con departamento (saludo + línea adicional)
greeting("Blake", "Software engineering")
greeting("Ellis", "Software engineering")


# La función print() muestra objetos en pantalla, separando con espacios
# cuando se pasan múltiples argumentos.
month = "September"
print("Investigate failed login attempts during", month, "if more than", 100)

# La función type() devuelve el tipo del argumento que recibe.
print(type("This is a string"))

# La función str() convierte a cadena cualquier dato (si es posible).
number = 12
string_representation = str(number)
print(string_representation)

# La función sorted() ordena una colección y devuelve una nueva lista ordenada
# sin modificar el iterable original.
time_list = [12, 2, 32, 19, 57, 22, 14]
print(sorted(time_list))  # Nueva lista ordenada
print(time_list)          # Lista original permanece igual

# Las funciones min() y max() devuelven el mínimo y máximo, respectivamente.
print(min(time_list))
print(max(time_list))
