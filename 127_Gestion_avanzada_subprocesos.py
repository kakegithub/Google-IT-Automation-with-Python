"""
Gestión avanzada de subprocesos: modificación del entorno (ENV) y PATH al invocar un comando.

Objetivo:
- Clonar el entorno actual del proceso (variables de entorno) y modificar PATH para anteponer
  un directorio específico ("/opt/myapp/") de modo que el sistema encuentre primero
  los ejecutables allí ubicados al ejecutar un comando.
- Ejecutar el binario/comando "myapp" usando el entorno personalizado.

Puntos clave:
- os.environ contiene las variables de entorno del proceso actual.
- Usar os.environ.copy() evita mutar el entorno global del proceso Python.
- PATH es una lista de rutas separadas por os.pathsep (":" en Unix). Anteponer una ruta
  hace que se prioricen ejecutables en esa ubicación.
- subprocess.run(..., env=my_env) permite pasar un entorno completo y aislado al subproceso.
- El código de retorno del comando queda en result.returncode; con check=True se lanzaría
  una excepción si es distinto de 0.
"""

import os
import subprocess

# Copiar las variables de entorno actuales para no modificar el entorno global del intérprete.
my_env = os.environ.copy()

# Construir un nuevo PATH anteponiendo "/opt/myapp/" al PATH existente.
# os.pathsep es el separador adecuado para el sistema (":" en Unix, ";" en Windows).
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

# Ejecutar el comando "myapp" usando el entorno personalizado, de modo que se resuelva
# primero en "/opt/myapp/". La salida va a stdout/stderr por defecto.
result = subprocess.run(["myapp"], env=my_env)

# Opcionalmente, se podría inspeccionar el código de salida:
# print(result.returncode)
