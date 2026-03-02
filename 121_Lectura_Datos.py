# cat streams.py
#!/usr/bin/env python3
"""
Demostración de lectura desde STDIN y escritura a STDOUT/STDERR en Python.

Flujo del script:
1) Lee texto desde la entrada estándar con input().
2) Escribe una respuesta en la salida estándar (stdout) usando print().
3) Intenta provocar un TypeError para que Python emita un traceback en STDERR (salida de errores).
4) Escribe explícitamente un mensaje en STDERR usando print(..., file=sys.stderr).

Notas:
- print() escribe por defecto en STDOUT.
- Las excepciones y tracebacks se imprimen en STDERR.
- También es posible escribir manualmente en STDERR pasando file=sys.stderr a print().
"""

import sys

# 1) Leer desde la entrada estándar (STDIN). El argumento es el prompt que se muestra al usuario.
data = input("This will come from STDIN: ")

# 2) Escribir en la salida estándar (STDOUT). Este es el comportamiento por defecto de print().
print("Now we write it to STDOUT: " + data)

# 3) Forzar un error de tipo (TypeError) para demostrar que las excepciones se emiten por STDERR.
#    Aquí se intenta concatenar una cadena con un entero (data + 1), lo que provoca un TypeError.
#    El traceback resultante aparecerá en STDERR y detendrá la ejecución del script antes de la siguiente línea.
print("Now we generate an error to STDERR: " + data + 1)

# 4) Escribir explícitamente en STDERR sin generar una excepción (esta línea no se ejecutará si ocurre el error anterior).
print("Now we write to STDERR: " + data + str(1), file=sys.stderr)

""" Ejecución de ejemplo (salida ilustrativa):
./streams.py
This will come from STDIN: Python Rocks!
Now we write it to STDOUT: Python Rocks!

# Se produce un TypeError al intentar sumar str con int, y Python imprime el traceback en STDERR:
Traceback (most recent call last):
  ...
TypeError: can only concatenate str (not 'int') to str

cat greeting.txt
Well hello there, STDOUT

cat greeting.txt
Well hello there, STDOUT

ls - z
"""
