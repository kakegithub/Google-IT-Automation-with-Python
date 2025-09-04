# Cálculo de almacenamiento asignado en bloques de 4096 bytes

def calculate_storage(filesize: int) -> int:
    """Calcula los bytes totales a asignar en disco para un archivo.

    Los sistemas de archivos suelen asignar espacio en bloques fijos.
    Aquí usamos un tamaño de bloque de 4096 bytes. Si el archivo no
    llena un bloque completo, se asigna un bloque adicional.

    Parámetros:
        filesize (int): Tamaño del archivo en bytes.

    Retorna:
        int: Bytes totales asignados (múltiplo de 4096).
    """
    block_size = 4096
    # División entera: cantidad de bloques completos ocupados
    full_blocks = filesize // block_size
    # Resto de bytes que no llenan un bloque completo
    remainder = filesize % block_size
    # Si hay resto, se necesita un bloque adicional
    if remainder > 0:
        full_blocks += 1
    # Bytes totales asignados
    return full_blocks * block_size


# Pruebas rápidas (salida esperada indicada a la derecha)
print(calculate_storage(1))      # 4096
print(calculate_storage(4096))   # 4096
print(calculate_storage(4097))   # 8192
print(calculate_storage(6000))   # 8192
