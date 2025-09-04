# Esta función convierte onzas líquidas (fluid ounces) a mililitros y 
# devuelve el resultado de la conversión.

def convert_volume(fluid_ounce: float) -> float:
    """
    Convierte un volumen en onzas líquidas (fl oz) a mililitros (ml).
    Aproximación: 1 fl oz ≈ 29.5 ml.
    """
    # Calcula el valor de "ml" usando el parámetro "fluid_ounce".
    ml = fluid_ounce * 29.5
    # Devuelve el resultado del cálculo.
    return ml


if __name__ == "__main__":
    # Llama a la conversión dentro de la función print() usando 2 onzas líquidas.
    # Convierte el valor de retorno de float a string para concatenarlo.
    print("The volume in milliliters is " + str(convert_volume(2)))

    # Vuelve a llamar a la función y duplica las 2 onzas líquidas desde la propia print.
    print("The volume in milliliters is " + str(convert_volume(2) * 2))

    # Cálculo alternativo equivalente (2 * 2 = 4 fl oz):
    # print("The volume in milliliters is " + str(convert_volume(4)))