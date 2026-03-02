#!/usr/bin/env python3

# Script interactivo que saluda al usuario y convierte una duración dada
# en horas, minutos y segundos a su equivalente en segundos.
#
# Flujo general:
# 1) Solicita el nombre del usuario y muestra un saludo.
# 2) Muestra un mensaje de bienvenida al conversor.
# 3) En un bucle, solicita horas, minutos y segundos, calcula el total en segundos
#    y lo muestra. Repite mientras el usuario responda 'y'.

# Solicita el nombre del usuario desde la entrada estándar
name = input("Please enter your name:")
# Imprime un saludo personalizado
print("Hello,  " + name)


def to_seconds(hours, minutes, seconds):
    """Convierte horas, minutos y segundos a segundos totales.

    Parámetros:
        hours (int): cantidad de horas
        minutes (int): cantidad de minutos
        seconds (int): cantidad de segundos
    Retorna:
        int: total de segundos (hours*3600 + minutes*60 + seconds)
    """
    return hours * 3600 + minutes * 60 + seconds


# Mensaje de bienvenida al conversor de tiempo
print("Welcome to this time converter")

# Variable de control del bucle. 'y' indica que el usuario desea continuar.
cont = "y"
while cont.lower() == "y":  # Se normaliza a minúsculas para aceptar 'Y' o 'y'
    # Solicita las partes de tiempo al usuario y las convierte a enteros
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))

    # Calcula y muestra el total de segundos usando la función to_seconds
    print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
    print()  # Línea en blanco para separar iteraciones y mejorar legibilidad

    # Pregunta si se desea realizar otra conversión. Cualquier respuesta distinta de 'y' detiene el bucle
    cont = input("Do you want to do another conversion? [y to continue] ")

# Mensaje final al salir del bucle
print("Goodbye!")
