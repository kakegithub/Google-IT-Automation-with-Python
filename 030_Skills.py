# Habilidades: control de flujo, funciones, operadores lógicos y aritméticos

# Skill 1
# Recordatorio de tareas según la hora recibida como cadena

def task_reminder(time_as_string: str) -> str:
    """Devuelve una tarea a realizar en función de la hora.

    Parámetros:
        time_as_string (str): Hora en formato como "8:00 a.m.".

    Retorna:
        str: Texto con la tarea sugerida.
    """
    # Selección por igualdad de cadenas con if/elif/else
    if time_as_string == "8:00 a.m.":
        task = "Check overnight backup images"
    elif time_as_string == "11:30 a.m.":
        task = "Run TPS report"
    elif time_as_string == "5:30 p.m.":
        task = "Reboot servers"
    else:
        # Valor por defecto si no coincide con ningún caso conocido
        task = "Provide IT Support to employees"

    return task


# Llamada de ejemplo
# Debería imprimir: "Provide IT Support to employees"
print(task_reminder("10:00 a.m."))
print()

# Skill 2
# Composición de funciones y aritmética básica

# Ejemplo 1: producto de productos

def product(a: int | float, b: int | float) -> int | float:
    """Retorna el producto a * b."""
    return a * b


# product(product(2, 4), product(3, 5)) = product(8, 15) = 120
print(product(product(2, 4), product(3, 5)))

#################################

# Ejemplo 2: diferencia de sumas
# Evitamos sombrear la función integrada sum() de Python usando 'add'.

def difference(a: int | float, b: int | float) -> int | float:
    """Retorna a - b."""
    return a - b


def add(a: int | float, b: int | float) -> int | float:
    """Retorna a + b (sumatoria)."""
    return a + b


# difference(add(2, 2), add(3, 3)) = difference(4, 6) = -2
print(difference(add(2, 2), add(3, 3)))

#################################

# Ejemplo 3: operadores lógicos con comparaciones
# (5 >= 8) es False y (5 <= 12) es True -> False and True -> False
print((5 >= 2 * 4) and (5 <= 4 * 3))

#################################

# Ejemplo 4: prioridad y cortocircuito en or
# x + 5 > x**2  =>  8 > 9 -> False;  x % 4 != 0  =>  3 % 4 != 0 -> True
# False or True -> True (se imprime el texto)

x = 3
if x + 5 > x ** 2 or x % 4 != 0:
    print("This comparison is True")

#################################

# Ejemplo 5: if/elif/else con aritmética y módulo
# number*2 < 14 => 12 < 14 -> True, por lo que imprime 6*6 % 3 -> 36 % 3 -> 0

number = 6
if number * 2 < 14:
    print(number * 6 % 3)
elif number > 7:
    print(100 / number)
else:
    print(7 - number)

# Sugerencia: si tienes problemas al calcular manualmente,
# revisa los materiales de estudio del módulo.

# Skill 3
# Resto fraccional normalizado (entre 0 y < 1), con casos especiales

def get_remainder(x: int, y: int) -> float:
    """Retorna (x % y) / y salvo en casos especiales donde retorna 0.

    Casos especiales:
        - x == 0 o y == 0 -> retorna 0 (evita división por cero, definida aquí).
        - x == y -> retorna 0 (porque el resto sería 0).

    Parámetros:
        x (int): Dividendo.
        y (int): Divisor.

    Retorna:
        float: Resto fraccional entre 0 (incl.) y 1 (excl.).
    """
    if x == 0 or y == 0 or x == y:
        return 0
    return (x % y) / y


# 10 % 3 = 1; 1 / 3 -> 0.333...
print(get_remainder(10, 3))
