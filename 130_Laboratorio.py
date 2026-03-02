#!/usr/bin/env python3
"""
Script para buscar errores en archivos de log.
Permite al usuario ingresar un término de error y busca coincidencias en un archivo de log.
"""

import sys
import os
import re


def error_search(log_file):
    """
    Busca errores en un archivo de log basado en la entrada del usuario.
    
    Args:
        log_file (str): Ruta del archivo de log a buscar
        
    Returns:
        list: Lista de líneas que contienen los errores encontrados
    """
    # Solicitar al usuario que ingrese el término de error a buscar
    error = input("What is the error? ")
    
    # Lista para almacenar los errores encontrados
    returned_errors = []
    
    # Abrir el archivo de log en modo lectura con codificación UTF-8
    with open(log_file, mode='r', encoding='UTF-8') as file:
        # Leer todas las líneas del archivo
        for log in file.readlines():
            # Crear lista de patrones de error
            # Comienza con "error" como patrón por defecto
            error_patterns = ["error"]
            
            # Dividir el término de error ingresado por espacios
            # y crear un patrón regex para cada palabra
            for i in range(len(error.split(' '))):
                # Convertir cada palabra a minúsculas y crear un patrón regex
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
            
            # Buscar coincidencias de los patrones en la línea actual
            for pattern in error_patterns:
                # Si se encuentra una coincidencia, agregar la línea a los resultados
                if re.search(pattern, log, re.IGNORECASE):
                    returned_errors.append(log)
                    break  # Evitar agregar la misma línea múltiples veces
    
    # Retornar la lista de errores encontrados
    return returned_errors


# Punto de entrada del script
if __name__ == "__main__":
    # Validar que se proporcionó un archivo de log como argumento
    if len(sys.argv) < 2:
        print("Error: Debes proporcionar un archivo de log como argumento")
        print("Uso: ./130_Laboratorio.py <archivo_log>")
        sys.exit(1)
    
    # Obtener el nombre del archivo de log desde los argumentos
    log_file = sys.argv[1]
    
    # Validar que el archivo existe
    if not os.path.exists(log_file):
        print(f"Error: El archivo '{log_file}' no existe")
        sys.exit(1)
    
    # Ejecutar la búsqueda de errores
    errors = error_search(log_file)
    
    # Mostrar los resultados
    if errors:
        print(f"\nSe encontraron {len(errors)} línea(s) con errores:")
        print("-" * 80)
        for error_line in errors:
            print(error_line.strip())
    else:
        print("No se encontraron errores en el archivo de log")
