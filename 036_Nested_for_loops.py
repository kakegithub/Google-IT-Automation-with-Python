# Bucles for anidados: ejemplos y explicaciones

# -----------------------------------------------------------------------------
# Ejemplo 1: pares ordenados [left|right] donde right comienza en 'left'
# Esto imprime una "matriz triangular" de combinaciones sin repetir
# casos donde right < left.
for left in range(7):
    for right in range(left, 7):
        print(f"[{left}|{right}]", end=" ")
    print()

# -----------------------------------------------------------------------------
# Ejemplo 2: calendario de enfrentamientos entre equipos
# Se generan emparejamientos en ambas direcciones (A vs B y B vs A),
# excluyendo los partidos de un equipo contra sí mismo.
teams = ["Dragons", "Wolves", "Pandas", "Unicorns"]
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(f"{home_team} vs {away_team}")

# -----------------------------------------------------------------------------
# Ejemplo 3: patrones típicos de anidamiento (comentados)
# for element in long_list:
#     do_something(element)
#
# for element1 in long_list:
#     for element2 in long_list:
#         do_something(element1, element2)

# -----------------------------------------------------------------------------
# Ejemplo 4: recorrer diccionario de listas con for anidados
estudiantes = {
    "grupo_a": ["Ana", "Juan", "Luis"],
    "grupo_b": ["Sofia", "Pablo", "Carmen"],
}

for grupo, nombres in estudiantes.items():
    print(f"Estudiantes del {grupo}:")
    for nombre in nombres:
        print(f"- {nombre}")

# -----------------------------------------------------------------------------
# Ejemplo 5: contar iteraciones en bucles for anidados
# El bucle externo se ejecuta 2 veces (x en 0..1) y el interno 4 veces (y en 0..3)
# por cada iteración externa; en total, 2 * 4 = 8 iteraciones internas.
for x in range(2):
    print(f"This is the outer loop iteration number {x}")
    for y in range(3 + 1):
        print(f"Inner loop iteration number {y}")
    print("Exit inner loop")
