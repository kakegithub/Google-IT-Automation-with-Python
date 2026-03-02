"""
Demostración de cómo capturar y manipular la salida de un comando del sistema con subprocess.run.

Se usa el comando: host 8.8.8.8
- capture_output=True redirige stdout y stderr a buffers en memoria (atributos .stdout y .stderr).
- El atributo .returncode indica el código de salida del proceso (0 éxito, !=0 error).
- .stdout es de tipo bytes; para trabajar como texto, se debe decodificar (por ej. .decode()).

Este script muestra:
1) El código de retorno del comando.
2) La salida cruda (bytes) del comando.
3) La salida decodificada, dividida en tokens (lista de palabras).

Notas:
- Si sólo se requiere texto directamente, se puede usar text=True (equivalente a universal_newlines=True)
  y entonces result.stdout será str en lugar de bytes.
- Para lanzar excepción en error, usar check=True.
"""

import subprocess

# Ejecuta el comando y captura su salida (stdout y stderr) sin imprimirla automáticamente.
result = subprocess.run(["host", "8.8.8.8"], capture_output=True)

# Imprime el código de retorno del comando ejecutado.
print(result.returncode)

# Imprime la salida estándar en bruto (tipo bytes).
print(result.stdout)

# Decodifica stdout (bytes -> str) usando la codificación por defecto (utf-8) y divide en tokens.
print(result.stdout.decode().split())
