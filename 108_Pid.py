"""
Este script define una función para extraer el ID de proceso (PID) y el tipo de mensaje
(por ejemplo, ERROR, RUNNING) de una línea de registro (log).
"""
import re


def extract_pid(log_line):
    """
    Extrae el PID y el tipo de mensaje de una línea de log.

    Args:
        log_line (str): La línea de registro a procesar.

    Returns:
        str: Una cadena con el formato "PID (TIPO_MENSAJE)" si se encuentra una coincidencia.
        None: Si el patrón no se encuentra en la línea de registro.
    """
    # El patrón busca un número entre corchetes (el PID) seguido de dos puntos,
    # un espacio y una palabra en mayúsculas (el tipo de mensaje).
    # (\d+): Captura el PID (uno o más dígitos).
    # ([A-Z]+): Captura el tipo de mensaje (una o más letras mayúsculas).
    regex = r"\[(\d+)\]: ([A-Z]+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    # Devuelve el PID (grupo 1) y el tipo de mensaje (grupo 2) formateados.
    return "{} ({})".format(result[1], result[2])


# --- Casos de prueba ---
# Debería imprimir: 12345 (ERROR)
print(extract_pid(
    "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"))
print(extract_pid("99 elephants in a [cage]"))  # None
print(extract_pid(
    "A string that also has numbers [34567] but no uppercase message"))  # None
# Debería imprimir: 67890 (RUNNING)
print(extract_pid(
    "July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup"))
