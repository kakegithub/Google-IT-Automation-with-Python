# Grupo de habilidades 1
# Comparaciones numéricas y de cadenas (lexicográficas por Unicode)

# 10*4 (40) es mayor que 14+23 (37) -> imprime True
print(10 * 4 > 14 + 23)  # Should print True

# 't'(116) no es menor que 's'(115); "tall" < "short" es False -> imprime False
print("tall" < "short")  # Should print False

print()


# Grupo de habilidades 2
# Esta función traduce ciertos códigos de error a mensajes descriptivos

def translate_error_code(error_code: str) -> str:
    """Traduce códigos de error HTTP a una descripción en texto.

    Parámetros:
        error_code (str): Código de error, por ejemplo "404 Not Found".

    Retorna:
        str: Descripción del error.
    """
    # Se usa una cascada if/elif/else para comparar por igualdad (==)
    if error_code == "401 Unauthorized":
        # Coincidencia exacta con 401
        translation = "Server received an unauthenticated request"
    elif error_code == "404 Not Found":
        # Coincidencia exacta con 404
        translation = "Requested web page not found on server"
    elif error_code == "408 Request Timeout":
        # Coincidencia exacta con 408
        translation = "Server request to close unused connection"
    else:
        # Cualquier otro código no contemplado
        translation = "Unknown error code"

    # Devuelve la traducción seleccionada
    return translation


# Muestra el resultado de traducir un código de error
# Salida esperada: "Requested web page not found on server"
print(translate_error_code("404 Not Found"))

print()


# Grupo de habilidades 3
# Estructura if/elif/else con múltiples comparaciones

number = 25  # Valor de ejemplo

# Se analiza number contra varios rangos/valores
if number <= 5:
    # Caso: 5 o menor
    print("The number is 5 or smaller.")
elif number == 33:
    # Caso: exactamente 33
    print("The number is 33.")
elif number < 32 and number >= 6:
    # Caso: entre 6 y 31 (inclusive 6, exclusivo 32)
    print("The number is less than 32 and greater than 6.")
else:
    # Cualquier otro caso
    print("The number is " + str(number))

# Salida esperada con number = 25: "The number is less than 32 and greater than 6."
print()


# Grupo de habilidades 4
# Redondeo a múltiplos de 10 hacia arriba si el resto es >= 5


def round_up(number: int) -> int:
    """Redondea un número al múltiplo de 10 más cercano.

    Reglas:
        - Si el resto al dividir entre 10 es >= 5, redondea hacia arriba.
        - En caso contrario, redondea hacia abajo al múltiplo de 10 inferior.

    Parámetros:
        number (int): Número a redondear.

    Retorna:
        int: Número redondeado al múltiplo de 10 más cercano según la regla.
    """
    base = 10
    whole_number = number // base  # División entera: 35 // 10 -> 3
    remainder = number % base      # Resto: 35 % 10 -> 5

    if remainder >= 5:
        # Redondeo hacia arriba
        return base * (whole_number + 1)

    # Redondeo hacia abajo
    return base * whole_number


# Llamada de ejemplo: 35 se redondea a 40
print(round_up(35))  # Should print 40
