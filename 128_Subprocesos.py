"""
Módulo de demostración de subprocesos en Python.
Compara tres formas de obtener el directorio actual:
- subprocess: ejecutando comandos del sistema
- os: usando el módulo os
- pathlib: usando el módulo pathlib

También demuestra diferentes métodos de subprocess:
- run(): ejecuta un comando y espera a que termine
- call(): ejecuta un comando y retorna el código de salida
- check_call(): como call() pero lanza excepción si falla
- check_output(): ejecuta un comando y retorna su salida
- Popen(): control avanzado de procesos
"""

import time
import subprocess
import os
from pathlib import Path

# ============================================================================
# 1. OBTENER DIRECTORIO ACTUAL CON DIFERENTES MÉTODOS
# ============================================================================

# Método 1: Usando subprocess - ejecuta el comando 'pwd' del sistema
cwd_subprocess = subprocess.check_output(['pwd'], text=True).strip()
print(f"Directorio actual (subprocess): {cwd_subprocess}")

# Método 2: Usando os - obtiene el directorio de trabajo actual
cwd_os = os.getcwd()
print(f"Directorio actual (os): {cwd_os}")

# Método 3: Usando pathlib - forma moderna de trabajar con rutas
cwd_pathlib = Path.cwd()
print(f"Directorio actual (pathlib): {cwd_pathlib}")

# ============================================================================
# 2. CREAR DIRECTORIOS CON DIFERENTES MÉTODOS
# ============================================================================

# Método 1: Usando subprocess - ejecuta el comando 'mkdir' del sistema
# La opción -p crea el directorio si no existe, sin error si ya existe
subprocess.run(['mkdir', '-p', 'test_dir_subprocess2'])
print("✓ Directorio listo con subprocess")

# Método 2: Usando os - crea un directorio
try:
    os.mkdir('test_dir_os2')
    print("✓ Directorio creado con os")
except FileExistsError:
    print("✓ El directorio ya existe (os)")

# Método 3: Usando pathlib - forma moderna de crear directorios
test_dir_pathlib2 = Path('test_dir_pathlib2')
# exist_ok=True asegura que no lance error si el directorio ya existe
test_dir_pathlib2.mkdir(exist_ok=True)
print("✓ Directorio creado con pathlib")

# ============================================================================
# 3. MÉTODOS DE SUBPROCESS
# ============================================================================

# subprocess.run() - Ejecuta un comando y espera a que termine
# Retorna un objeto CompletedProcess
result_run = subprocess.run(
    ['echo', 'Hello, World!'], capture_output=True, text=True)
print(f"\nsubprocess.run() - stdout: {result_run.stdout.strip()}")

# subprocess.call() - Ejecuta un comando y retorna el código de salida
# 0 = éxito, otros valores = error
return_code_call = subprocess.call(['echo', 'Hello from call!'])
print(f"subprocess.call() - código de retorno: {return_code_call}")

# subprocess.check_call() - Como call() pero lanza excepción si falla
# Retorna el código de salida (0 si éxito)
return_code_check_call = subprocess.check_call(
    ['echo', 'Hello from check_call!'])
print(f"subprocess.check_call() - código de retorno: {return_code_check_call}")

# subprocess.check_output() - Ejecuta un comando y retorna su salida
# Lanza excepción si el comando falla
output_check_output = subprocess.check_output(
    ['echo', 'Hello from check_output!'], text=True)
print(f"subprocess.check_output() - stdout: {output_check_output.strip()}")

# ============================================================================
# 4. SUBPROCESS.POPEN() - CONTROL AVANZADO DE PROCESOS
# ============================================================================

# Popen() proporciona control más granular sobre el proceso
# stdout=subprocess.PIPE captura la salida estándar
process_popen = subprocess.Popen(
    ['echo', 'Hello from popen!'], stdout=subprocess.PIPE, text=True)

# communicate() espera a que el proceso termine y retorna (stdout, stderr)
output_popen, _ = process_popen.communicate()
print(f"subprocess.Popen() - stdout: {output_popen.strip()}")

# ============================================================================
# 5. DEMOSTRACIÓN DE COMPORTAMIENTO ASINCRÓNICO
# ============================================================================

# Crear un proceso que duerme 5 segundos
process = subprocess.Popen(['sleep', '5'])

message_1 = "El proceso se está ejecutando en segundo plano..."

# Esperar 2 segundos para demostrar el comportamiento asincrónico
time.sleep(2)

# poll() retorna None si el proceso sigue ejecutándose
# Retorna el código de salida si el proceso ha terminado
if process.poll() is None:
    message_2 = "El proceso aún se está ejecutando."
else:
    message_2 = "El proceso ha terminado."

print(f"\n{message_1}")
print(message_2)
