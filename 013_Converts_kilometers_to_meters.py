# 1) La función convierte kilómetros (km) a metros (m)
def convert_distance(km):
    """Convierte una distancia en kilómetros a metros.

    Parámetros:
        km (float | int): Distancia en kilómetros.

    Retorna:
        float: Distancia convertida a metros.
    """
    m = km * 1000  # 1 kilómetro equivale exactamente a 1000 metros
    return m


# No indentes las siguientes líneas de código; deben estar
# fuera de la función definida arriba.


# Distancia del viaje en kilómetros
my_trip_kilometers = 55


# 2) Convierte my_trip_kilometers a metros llamando a la función anterior
my_trip_meters = convert_distance(my_trip_kilometers)


# 3) Imprime el resultado de convertir my_trip_kilometers a metros
print("The distance in meters is " + str(my_trip_meters))
