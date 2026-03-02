"""
Demostración de uso de argumentos de línea de comandos (sys.argv), verificación de códigos de salida
($?), y creación condicional de archivos usando os.path y sys.exit.

Este archivo contiene, dentro de un string multilínea, ejemplos de comandos de terminal y
un script de ejemplo que ilustra cómo acceder a los argumentos pasados al script y cómo
utilizar códigos de salida para indicar éxito o error.

Secciones de ejemplo incluidas (comentadas como referencia):
- Mostrar sys.argv con diferentes invocaciones.
- Consultar el código de salida del último comando con 'echo $?'.
- Script que crea un archivo si no existe, o termina con error si ya existe.
"""

# Bloque de referencia: ejemplos de terminal y un script de ejemplo (no se ejecuta, es documentación)
""" import os
import sys
cat parameters.py
#!/usr/bin/env python3
print(sys.argv)

./parameters.py
['./parameters.py']

./parameters.py one two three
['./parameters.py', 'one', 'two', 'three']


wc variables.py
7 19 174 variables.py
echo $?
0

wc notpresent.sh
wc: notpresent.sh: No such file or directory
echo $?
1

#!/usr/bin/env python3


filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created\n")
else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)

./create_file.py example
echo $?
 """

# Nota: El contenido anterior está como documentación. A continuación se ofrece el mismo
# ejemplo de creación de archivo con comentarios, listo para ejecutarse si se desea.

import os
import sys

# Verificar que se proporcione exactamente un argumento (el nombre del archivo a crear).
# sys.argv es la lista de argumentos: argv[0] es el nombre del script, argv[1] el primer argumento, etc.
if len(sys.argv) != 2:
    print("Uso: python3 123_Argumentos_linea_comandos.py <nombre_archivo>")
    # Código de salida 2 indica error de uso/argumentos inválidos (convención común)
    sys.exit(2)

filename = sys.argv[1]

# Si el archivo no existe, lo creamos y escribimos una línea de texto.
if not os.path.exists(filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("New file created\n")
    # Código de salida implícito 0 (éxito) al finalizar el script sin llamar a sys.exit con error.
    print(f"Archivo creado: {filename}")
else:
    # Si el archivo ya existe, informamos y salimos con código de error 1.
    print(f"Error, el archivo {filename} ya existe!")
    sys.exit(1)
