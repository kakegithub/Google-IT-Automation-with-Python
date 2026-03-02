#!/usr/bin/env python3
"""
Script para filtrar y contar usuarios en archivos de registro (logs).
Busca entradas de CRON en un archivo de log y cuenta cuántas veces aparece cada usuario.

Uso: ./129_Filtrado_archivos_registro.py <archivo_log>
Ejemplo: ./129_Filtrado_archivos_registro.py syslog
"""

import re
import sys

# ============================================================================
# 1. INICIALIZACIÓN Y DEMOSTRACIÓN DEL DICCIONARIO
# ============================================================================

# Diccionario para almacenar el conteo de usuarios
# Clave: nombre de usuario, Valor: número de apariciones
usernames = {}

# Nombre de usuario de prueba
name = "good_user"

# Incrementar el contador del usuario usando get()
# get(name, 0) retorna el valor si existe, o 0 si no existe
# Luego suma 1 al resultado
usernames[name] = usernames.get(name, 0) + 1
print(f"Después del primer incremento: {usernames}")

# Incrementar nuevamente el contador del mismo usuario
usernames[name] = usernames.get(name, 0) + 1
print(f"Despu��s del segundo incremento: {usernames}")

# ============================================================================
# 2. LECTURA Y PROCESAMIENTO DEL ARCHIVO DE LOG
# ============================================================================

# Validar que se proporcionó un argumento de línea de comandos
if len(sys.argv) < 2:
    print("Error: Debes proporcionar un archivo de log como argumento")
    print("Uso: ./129_Filtrado_archivos_registro.py <archivo_log>")
    sys.exit(1)

# Obtener el nombre del archivo de log desde los argumentos de línea de comandos
# sys.argv[0] es el nombre del script, sys.argv[1] es el primer argumento
log_file = sys.argv[1]

# Abrir el archivo de log en modo lectura
with open(log_file) as f:
    # Iterar sobre cada línea del archivo
    for line in f:
        # Filtrar: solo procesar líneas que contengan "CRON"
        # Si la línea no contiene "CRON", saltar a la siguiente iteración
        if "CRON" not in line:
            continue
        
        # Patrón de expresión regular para extraer el nombre de usuario
        # Busca: USER (nombre_usuario)
        # (\w+) captura uno o más caracteres de palabra (el nombre de usuario)
        # $ indica el final de la línea
        pattern = r"USER \((\w+)\)$"
        
        # Buscar el patrón en la línea actual
        # search() retorna un objeto Match si encuentra coincidencia, None si no
        result = re.search(pattern, line)
        
        # Verificar si se encontró una coincidencia
        if result is None:
            # Si no hay coincidencia, saltar a la siguiente línea
            continue
        
        # Extraer el nombre de usuario del grupo capturado (grupo 1)
        # result[1] obtiene el contenido del primer grupo de captura (\w+)
        name = result[1]
        
        # Incrementar el contador del usuario en el diccionario
        # Si el usuario no existe, comienza en 0 y suma 1
        # Si ya existe, suma 1 al valor actual
        usernames[name] = usernames.get(name, 0) + 1

# ============================================================================
# 3. MOSTRAR RESULTADOS FINALES
# ============================================================================

# Imprimir el diccionario final con el conteo de usuarios
print(f"\nConteo final de usuarios en CRON: {usernames}")

# ============================================================================
# NOTAS IMPORTANTES
# ============================================================================
# - El script espera un archivo de log como argumento
# - Solo procesa líneas que contengan "CRON"
# - Extrae nombres de usuario usando expresiones regulares
# - Cuenta cuántas veces aparece cada usuario
# - El diccionario usernames almacena los resultados finales
#
# Ejecución: ./129_Filtrado_archivos_registro.py syslog
