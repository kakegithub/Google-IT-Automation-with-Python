# Bucles infinitos: cómo ocurren y cómo evitarlos
# Este archivo muestra patrones correctos para evitar bucles infinitos y errores.

# -----------------------------------------------------------------------------
# Ejemplo 1: dividir entre 2 mientras sea par (con protección contra 0)
# Si x es 0, la condición x % 2 == 0 es True y x //= 2 mantiene x en 0
# para siempre (bucle infinito). Por eso, se añade x != 0.

x: int = 0
while x != 0 and x % 2 == 0:
    x //= 2
print(f"Ejemplo 1 -> x inicial=0, el bucle no ejecuta, x final={x}")

# -----------------------------------------------------------------------------
# Ejemplo 2: misma idea usando un if como guarda delante del while

x = 64
if x != 0:
    while x % 2 == 0:
        x //= 2
print(f"Ejemplo 2 -> x final tras dividir pares sucesivos: {x}")  # 1

# -----------------------------------------------------------------------------
# Ejemplo 3: solo por pares (sin guarda), pero usando un valor seguro (64)
# Nota: si x fuese 0, esto sería un bucle infinito. Evítalo con una guarda.

x = 64
while x % 2 == 0:
    x //= 2
print(f"Ejemplo 3 -> x final (sin guarda con x=64): {x}")  # 1

# -----------------------------------------------------------------------------
# Ejemplo 4: bucle while True con break (patrón correcto)
# Se implementan funciones de ejemplo para evitar NameError y controlar la salida.


def do_something_cool(step: int) -> None:
    """Función de ejemplo: hace 'algo' en cada iteración."""
    print(f"Doing something cool at step {step}...")


def user_requested_to_stop(step: int) -> bool:
    """Simula una petición de parada después de 3 iteraciones."""
    return step >= 3


step = 0
while True:
    step += 1
    do_something_cool(step)

    if user_requested_to_stop(step):
        break

print("Bucle detenido por condición de corte (break)")
