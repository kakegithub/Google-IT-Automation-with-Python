######################################################################################

#    string.lower() - Devuelve una copia de la cadena con todos los caracteres en minúsculas
print("AaBbCcDdEe".lower())  # prints "aabbccddee"

########################################################################################


#########################################################################################

#    string.upper() - Devuelve una copia de la cadena con todos los caracteres en mayúsculas
print("AaBbCcDdEe".upper())  # prints "AABBCCDDEE"


#############################################################################################


#############################################################################################

#    string.lstrip() - Devuelve una copia de la cadena sin los espacios en blanco del lado izquierdo
print("  Hello  ".lstrip())  # prints "Hello   "

################################################################################################


#####################################################################################################

#     string.rstrip() - Devuelve una copia de la cadena sin los espacios en blanco del lado derecho
print("  Hello  ".rstrip())  # prints "   Hello"

#########################################################################################################


##########################################################################################################

#    string.strip() - Devuelve una copia de la cadena sin los espacios en blanco de los lados izquierdo y derecho
print("   Hello   ".strip())  # prints "Hello"

################################################################################################################


#################################################################################################################

#    string.count(substring)- Devuelve el número de veces que la subcadena está presente en la cadena
test = "How much wood would a woodchuck chuck"
print(test.count("wood"))  # prints 2

###################################################################################################################


#####################################################################################################################

#    string.isnumeric() - Devuelve True si sólo hay caracteres numéricos en la cadena. En caso contrario, devuelve False.
print("12345".isnumeric())  # prints True
print("-123.45".isnumeric())  # prints False

#########################################################################################################################


##########################################################################################################################

#    string.isalpha() - Devuelve True si sólo hay letras en la cadena. En caso contrario, devuelve False.
print("xyzzy".isalpha())  # prints True

###########################################################################################################################


###########################################################################################################################

#    string.split() - Devuelve una lista de subcadenas separadas por espacios en blanco (un espacio en blanco puede ser un espacio, un tabulador o una nueva línea)
print(
    test.split()
)  # prints ['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck']

##############################################################################################################################


#################################################################################################################################

#    string.split(delimiter) - Devuelve una lista de subcadenas separadas por espacios en blanco u otra cadena
test = "How-much-wood-would-a-woodchuck-chuck"
print(
    test.split("-")
)  # prints ['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck']

####################################################################################################################################


#######################################################################################################################################

#    string.replace(old, new) - Devuelve una nueva cadena donde todas las apariciones de old han sido reemplazadas por new.
print(
    test.replace("wood", "plastic")
)  # prints "How much plastic would a plasticchuck chuck"

###########################################################################################################################################


#############################################################################################################################################
#    delimiter.join(list of strings) - Devuelve una nueva cadena con todas las cadenas unidas por el delimitador
print("-".join(test.split()))  # prints "How-much-wood-would-a-woodchuck-chuck"

#####################################################################################################################################
