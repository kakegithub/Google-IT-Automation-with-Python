#!/usr/bin/env python3
import os

# Este script muestra el valor de algunas variables de entorno.
# Usamos os.environ.get("VAR", "") para leer una variable de entorno
# devolviendo una cadena vacía si la variable no existe.

print("HOME: " + os.environ.get("HOME", ""))   # Directorio home del usuario
print("SHELL: " + os.environ.get("SHELL", "")) # Intérprete por defecto (bash, zsh...)
print("FRUIT: " + os.environ.get("FRUIT", "")) # Ejemplo de variable personalizada

# Ejemplos de comandos en la terminal relacionados con este script:
# Mostrar la variable PATH:
#   echo $PATH
# (Salida típica): /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# Establecer una variable de entorno temporal y ejecutar el script:
#   export FRUIT=Pineapple
#   ./variables.py
