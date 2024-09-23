#######################################################################################################################


x = ["Now", "we", "are", "cooking!"]

type(x)

print(x)

len(x)  # 4

"are" in x  # True

"Today" in x  # False

print(x[0])  #  "Now"
print(x[3])  # "cooking!"

# print(x[4])   # This last line will throw an error

x[1:3]  # ['we', 'are']

x[:2]  # ['Now', 'we']

x[2:]  # ['are', 'cooking!']


########################################################################################################################


def get_word(sentence, n):
    # Solo procede si n es positivo
    if n > 0:
        words = sentence.split()
        # Solo procede si n no es mayor que el número de palabras
        if n <= len(words):
            return words[n - 1]  # Acceder al índice n-1 ya que el índice comienza en 0
    return ""


# Pruebas de la función
print(get_word("This is a lesson about lists", 4))  # Debe imprimir: lesson
print(get_word("This is a lesson about lists", -4))  # No debe imprimir nada
print(get_word("Now we are cooking!", 1))  # Debe imprimir: Now
print(get_word("Now we are cooking!", 5))  # No debe imprimir nada


##############################################################################################################################
