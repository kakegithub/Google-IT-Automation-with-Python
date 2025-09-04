# Listas y tuplas: creación, desempaquetado y funciones de utilidad

# Tupla de ejemplo (inmutable)
fullname = ("Grace", "M", "Hooper")


# -----------------------------------------------------------------------------
# Función: convertir segundos a (horas, minutos, segundos)

def convert_seconds(seconds: int) -> tuple[int, int, int]:
    """Convierte una cantidad de segundos en (horas, minutos, segundos).

    Retorna una tupla con los tres componentes enteros.
    """
    hours, rem = divmod(seconds, 3600)
    minutes, remaining_seconds = divmod(rem, 60)
    return hours, minutes, remaining_seconds


# Ejemplos de uso con tuplas y desempaquetado
result = convert_seconds(5000)
print(result)  # (horas, minutos, segundos)

hours, minutes, seconds = result
print(hours, minutes, seconds)

hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds)


# -----------------------------------------------------------------------------
# Función: formatear tamaño de archivo en KiB con 2 decimales

def file_size(file_info: tuple[str, str, int]) -> str:
    """Recibe (nombre, tipo, tamaño_en_bytes) y retorna el tamaño en KiB con 2 decimales."""
    name, file_type, size_bytes = file_info
    return f"{size_bytes / 1024:.2f}"


print(file_size(("Class Assignment", "docx", 17875)))  # Should print 17.46
print(file_size(("Notes", "txt", 496)))                 # Should print 0.48
print(file_size(("Program", "py", 1239)))               # Should print 1.21
