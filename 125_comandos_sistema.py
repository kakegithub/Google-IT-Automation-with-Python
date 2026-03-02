"""
Demostración de ejecución de comandos del sistema usando subprocess.run.

Pasos que realiza el script:
1) Ejecuta el comando 'date' y deja que su salida se imprima directamente en la terminal.
2) Pausa 2 segundos ejecutando 'sleep 2'.
3) Intenta listar un archivo inexistente con 'ls this_file_does_not_exist' para provocar un error
   y obtener su código de retorno.
4) Imprime el código de retorno del último comando ejecutado.

Notas útiles sobre subprocess.run:
- Por omisión, la salida/errores de los comandos se envían directamente a stdout/stderr del proceso padre.
- Para capturar la salida en variables, usar capture_output=True (o stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  y text=True para cadenas en lugar de bytes.
- Para que lance una excepción cuando el comando devuelva código distinto de 0, usar check=True.
- El código de retorno está disponible en result.returncode (0 = éxito, distinto de 0 = error).
"""

import subprocess

# Ejecuta el comando 'date'. La salida se mostrará en la terminal estándar.
subprocess.run(["date"])  # Ejemplo de ejecución simple sin captura de salida

# Pausa por 2 segundos ejecutando el comando 'sleep 2'.
subprocess.run(["sleep", "2"])  # También podría hacerse en Python con time.sleep(2)

# Intenta listar un archivo que no existe para observar un código de retorno de error.
# No usamos check=True para evitar que se lance una excepción; así podemos examinar returncode.
result = subprocess.run(["ls", "this_file_does_not_exist"])  

# Muestra el código de retorno del comando anterior (0 = éxito, != 0 = error)
print(result.returncode)
