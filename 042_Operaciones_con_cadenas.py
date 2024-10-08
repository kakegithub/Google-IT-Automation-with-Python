###############################################################################
# len(string) - Devuelve la longitud de la cadena

print(len("abcde"))

# prints 5

################################################################################


################################################################################
# for character in string - Iterar sobre cada carácter de la cadena
for c in "abcde":
    print(c)

# prints "a", then "b", then "c", etc.

#################################################################################


##################################################################################
#     if substring in string - Comprueba si la subcadena forma parte de la cadena
print("abc" in "abcde")  # prints True
print("def" in "abcde")  # prints False

####################################################################################

####################################################################################
#    string[i] - Accede al carácter en el índice i de la cadena, comenzando en cero
print("abcde"[2])  # prints "c"
print("abcde"[-1])  # prints "e"

####################################################################################

#####################################################################################
print("abcde"[0:2])  # prints "ab"
print("abcde"[2:])  # prints "cde"

#####################################################################################
