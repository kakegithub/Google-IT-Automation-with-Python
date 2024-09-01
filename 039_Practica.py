##############################################################
number = 2  # Initialize the variable
while number <= 12:  # Complete the while loop condition
    print(number, end=" ")
    number += 2  # Increment the variable

# Should print 2 4 6 8 10 12
################################################################

################################################################
for number in range(2, 12 + 1, 2):
    print(number)

# Should print:
# 2
# 4
# 6
# 8
# 10
# 12
##################################################################


###################################################################
# Esta función debe contar cuántos números pares existen en una secuencia desde 0 hasta el número "n" dado, donde 0 cuenta como número par.  Por ejemplo, números_pares(25) debería devolver 13, y números_pares(6) debería devolver 4.
def even_numbers(n):
    count = 0
    current_number = 0
    while current_number <= n:  # Complete the while loop condition
        if current_number % 2 == 0:
            count += 1  # Increment the appropriate variable
        current_number += 1  # Increment the appropriate variable
    return count


print(even_numbers(25))  # Should print 13
print(even_numbers(144))  # Should print 73
print(even_numbers(1000))  # Should print 501
print(even_numbers(0))  # Should print 1
###################################################################################


##################################################################################
def multiplication_table(start, stop):
    # Complete the outer loop range
    for x in range(start, stop + 1):
        # Complete the inner loop range
        for y in range(start, stop + 1):
            # Prints the value of "x" multiplied by "y"
            # and inserts a space after each value
            print(str(x * y), end=" ")
        # An empty print() function inserts a line break at the
        # end of the row
        print()


multiplication_table(1, 3)
# Should print the multiplication table shown above
########################################################################################


##########################################################################################
#  Esta función debe comenzar en la variable "start", que es un número entero que se pasa a la función, y realizar una cuenta atrás hasta 0. Complete el código para que una llamada a la función como "countdown(2)" devuelva los números "2,1,0".


def countdown(start):
    x = start
    if x > 0:
        return_string = "Counting down to 0: "
        while x >= 0:  # Complete the while loop
            return_string += str(x)  # Add the numbers to the "return_string"
            if x > 0:
                return_string += ","
            x -= 1  # Decrement the appropriate variable
    else:
        return_string = "Cannot count down to 0"
    return return_string


print(countdown(10))  # Should be "Counting down to 0: 10,9,8,7,6,5,4,3,2,1,0"
print(countdown(2))  # Should be "Counting down to 0: 2,1,0"
print(countdown(0))  # Should be "Cannot count down to 0"

##################################################################################################

####################################################################################################

# Esta función debe devolver una cadena separada por espacios de todos los números, desde la variable "mínimo" inicial hasta la variable "máximo" que se pasa a la función, inclusive.


def all_numbers(minimum, maximum):

    return_string = ""  # Initializes variable as a string

    # Complete the for loop with a range that includes all
    # numbers up to and including the "maximum" value.
    for x in range(minimum, maximum + 1):

        # Complete the body of the loop by appending the number
        # followed by a space to the "return_string" variable.
        return_string += str(x) + " "

    # This .strip command will remove the final " " space
    # at the end of the "return_string".
    return return_string.strip()


print(all_numbers(2, 6))  # Should be 2 3 4 5 6
print(all_numbers(3, 10))  # Should be 3 4 5 6 7 8 9 10
print(all_numbers(-1, 1))  # Should be -1 0 1
print(all_numbers(0, 5))  # Should be 0 1 2 3 4 5
print(all_numbers(0, 0))  # Should be 0

#################################################################################################3
