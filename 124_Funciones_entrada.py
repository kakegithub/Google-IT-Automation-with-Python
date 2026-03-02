#!/usr/bin/env python3
"""
Demostración de funciones de entrada y evaluación en Python.

Flujo del script:
1) Solicita un valor por teclado con input().
2) Imprime el valor recibido (como texto) en STDOUT.
3) Muestra cómo type() sobre la variable devuelve su tipo (aunque aquí su valor no se imprime).
4) Evalúa la cadena ingresada con eval() para convertirla a un literal/expresión Python.

Advertencias:
- input() siempre retorna una cadena (str).
- eval() ejecuta la expresión suministrada: NO es seguro usarlo con entradas no confiables
  pues puede ejecutar código arbitrario. Para convertir números, es preferible usar int(), float(),
  o ast.literal_eval() para evaluar literales de forma segura.

Ejemplo:
Entrada: "123" -> print(my_number) muestra "123" (str). eval("123") da el entero 123.
"""

import sys  # Importado por si se requieren futuras operaciones con stdin/stdout/stderr

# 1) Solicita al usuario un número (en realidad se leerá como texto).
my_number = input("Please enter a number: ")

# 2) Muestra en pantalla lo ingresado (aún es tipo str).
print(my_number)

# 3) Llamada a type(my_number) que devuelve <class 'str'>, pero su resultado no se imprime ni se usa.
#    Si se quisiera mostrar, usar: print(type(my_number))
type(my_number)

# 4) Evalúa el contenido textual como una expresión Python.
#    Peligroso con entradas no confiables. Para números: usar int(my_number) o float(my_number).
eval(my_number)
