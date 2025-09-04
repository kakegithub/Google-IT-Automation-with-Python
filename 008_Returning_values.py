"""
Demostración de funciones que retornan valores:
- Cálculo de área de un triángulo
- Suma de áreas de dos triángulos
- Conversión de segundos a (horas, minutos, segundos)
- Función de saludo que retorna un string

Correcciones aplicadas:
- Se evita sombrear la función incorporada sum() renombrando la variable a
  'sum_areas'.
- Se modifica greeting() para que retorne el saludo en lugar de imprimirlo,
  evitando que al imprimir su resultado aparezca 'None'.
"""

# Cálculo del área de un triángulo

def area_triangle(base, height):
    """Devuelve el área de un triángulo como base * altura / 2."""
    return base * height / 2


# Suma de las áreas de dos triángulos
area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)

# Evitamos usar el nombre 'sum' para no ocultar la función incorporada sum()
sum_areas = area_a + area_b
print(f"The sum of both areas is: {sum_areas}")


# Conversión de segundos a horas, minutos y segundos

def convert_seconds(seconds):
    """Convierte 'seconds' en una tupla (hours, minutes, remaining_seconds)."""
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

# Desempaquetamos la tupla devuelta por la función
hours, minutes, secs = convert_seconds(5000)
print(hours, minutes, secs)


# Función que retorna un saludo (en lugar de imprimir directamente)

def greeting(name):
    """Retorna un saludo para el nombre dado."""
    return "Welcome, " + name

result = greeting("Christine")
print(result)
