# Destreza 1: Uso de métodos de cadena

#     Separe los valores numéricos de los valores de texto en una cadena utilizando .split().

#     Iterar sobre los elementos de una cadena.

#     Compruebe si el elemento contiene letras con .isalpha().

#     Asigna los elementos de la cadena dividida a nuevas variables.

#     Recorte los espacios en blanco sobrantes con .strip().

#     Formatea una cadena utilizando .format() y marcadores de posición de variables { } .


def sales_price(item_and_price):
    # Inicializa variables "item" and "price" as strings.
    item = ""
    price = ""

    # Create a variable "item_or_price" to hold the result of the split.
    item_or_price = item_and_price.split()

    # For each element "x" in the split variable "item_or_price"
    for x in item_or_price:
        # Check if the element is a letter
        if x.isalpha():
            # If true, assign the element to the "item" string variable and add a space
            # for any item names containing multiple words, like "Winter fleece jacket".
            item += x + " "
            # Else, if x is a number (if x.isalpha() is false):
        else:
            # Assign the element to the "price" string variable.
            price = x
    # Strip the extra space to the right of the last "item" word
    item = item.strip()

    # Return the item name and price formatted in a sentence
    return "{} are on sale for ${}".format(item, price)

    # Call to the function
    print(sales_prices("Winter fleece jackets 49.99"))
    # Should print "Winter fleece jackets are on sale for $49.99"


###############################################################################################################3
