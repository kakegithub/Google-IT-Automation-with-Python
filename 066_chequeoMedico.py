#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Este script realiza una verificación del estado del sistema,
comprobando el uso del disco y el uso de la CPU.
"""
import shutil  # Importa el módulo shutil para operaciones de alto nivel con archivos y directorios
import psutil  # Importa el módulo psutil para obtener información del sistema y los procesos


def check_disk_usage(disk):
    """
    Verifica si el espacio libre en disco es mayor al 20%.
    Args:
        disk (str): La ruta al disco a verificar (ej: "/").
    Returns:
        bool: True si el espacio libre es mayor al 20%, False de lo contrario.
    """
    du = shutil.disk_usage(disk)  # Obtiene la información del uso del disco
    free = du.free / du.total * 100  # Calcula el porcentaje de espacio libre
    return free > 20  # Retorna True si el espacio libre es mayor al 20%, False de lo contrario


def check_cpu_usage():
    """
    Verifica si el uso de la CPU es menor al 75%.
    Returns:
        bool: True si el uso de la CPU es menor al 75%, False de lo contrario.
    """
    usage = psutil.cpu_percent(1)  # Obtiene el porcentaje de uso de la CPU durante 1 segundo
    return usage < 75  # Retorna True si el uso de la CPU es menor al 75%, False de lo contrario


# Verifica si el espacio libre en disco es menor al 20% o si el uso de la CPU es mayor al 75%
if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR: Not enough disk space or CPU usage is too high.")  # Imprime un mensaje de error si alguna de las condiciones no se cumple
else:
    print("Everything is fine.")  # Imprime un mensaje de que todo está bien si ambas condiciones se cumplen
