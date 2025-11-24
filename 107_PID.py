import re

# --- Bloque 1: Búsqueda exitosa ---
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
# Imprime el primer grupo capturado: '12345'
print(result[1])


# --- Bloque 2: Sobrescribir el resultado con otra búsqueda exitosa ---
result = re.search(
    regex, "A completely different string that also has numbers [34567]")
# Imprime el nuevo grupo capturado: '34567'
print(result[1])


# --- Bloque 3: Búsqueda fallida y el error ---
# Esta búsqueda falla porque "[cage]" no contiene dígitos (\d+).
# re.search devuelve None.
result = re.search(regex, "99 elephants in a [cage]")

# La siguiente línea causaría un error: TypeError: 'NoneType' is not subscriptable
# porque `result` es None. La comentamos para que el script pueda continuar.
# print(result[1])
print("La búsqueda en '[cage]' no encontró un PID, devolvió:", result)


# --- Bloque 4: La solución con una función robusta ---
def extract_pid(log_line):
    """
    Extrae el PID de una línea de log.
    Devuelve el PID como una cadena o una cadena vacía si no se encuentra.
    """
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    # Comprobación para evitar el error: si no hay resultado, devuelve algo seguro.
    if result is None:
        return ""
    return result[1]


# Probando la función con los diferentes casos:
print("PID del log original:", extract_pid(log))  # Devuelve '12345'
print("PID de '[cage]':", extract_pid(
    "99 elephants in a [cage]"))  # Devuelve ""
