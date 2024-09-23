# Puedes crear una lista a partir de un iterable utilizando un bucle for, que es una forma útil de iterar sobre un iterable:

""" new_list = []
for thing in list_of_things:
    new_list.append[do_something(thing)]

 """

#########################################################################################################################################

#  Una comprensión de lista permite crear una nueva lista a partir de un iterable en una sola línea. Esta línea consigue el mismo resultado que el bucle for anterior, pero de una forma más concisa:

# new_list = [do_something(thing) for thing in list_of_things]

#############################################################################################################################################


# Create a list of tuples where each tuple contains the numbers 1, 2, and 3.
numbers = [(1, 2, 3) for _ in range(5)]

print(numbers)

###############################################################################################################################################


### Simple List Comprehension
print("List comprehension result:")

# The following list comprehension compacts several lines
# of code into one line:
print([x * 2 for x in range(1, 11)])

### Long form for loop
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code shown below:
my_list = []
for x in range(1, 11):
    my_list.append(x * 2)
print(my_list)

# Select Run to compare the two results.

##################################################################################################################################################

# Comprensión de lista con Sentencia condicional

print("List comprehension result:")
print([x for x in range(1, 101) if x % 10 == 0])

# The list comprehension above accomplishes the same result as
# the long form version of the code:
print("Long form code result:")
my_list = []
for x in range(1, 101):
    if x % 10 == 0:
        my_list.append(x)
print(my_list)

# Select Run to observe the two results.

####################################################################################################################################################


def squares(start, end):
    return [n**2 for n in range(start, end + 1)]


print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10))  # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#######################################################################################################################################################
