x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))

#####################################################


def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")


attempts(5)
########################################################
""" username = get_username()
while not valid_username(username):
    print("Invalid username")
    username = get_username() """
# This code will give an error because get_username is not defined

##########################################################

""" while my_variable < 10:
    print("Hello")
    my_variable += 1 """
# This code will give a NameError
# Variable is not defined

#############################################################
my_variable = 5
while my_variable < 10:
    print("Hello")
    my_variable += 1
###########################################################3
x = 1
sum = 0
while x < 10:
    sum = sum + x
    x = x + 1

product = 1
while x < 10:
    product = product * x
    x = x + 1

print(sum, product)
# Ouput 45 1
# This code contains an error, but it will not give an error when the code is run. The problem here is that product should be set to product = x. In this code, x is never initialized so this code is false before it is even run. The product variable has the wrong value
############################################################
multiplier = 1
result = multiplier * 5
while result <= 50:
    print(result)
    multiplier += 1
    result = multiplier * 5
print("Done")


# This while loop prints the multiples of 5 between 1 and 50. The
# "multiplier" variable is initialized with the starting value of 1.
# The "result" variable is initialized with the value of the
# "multiplier" variable times 5.

# The while loop specifies that the loop must iterate while it is True
# that the "result" is less than or equal to 50. Within the while loop,
# the code tells the Python interpreter to print the value of the
# "result" variable. Then, the "multiplier" is incremented by 1 and the
# "result" is assigned the new value of the "multiplier" times 5.

# The end of the while loop is indicated by the indentation of the next
# line of code moving one tab to the left. At this point, the Python
# interpreter automatically loops back to the beginning of the while
# loop to check the condition again with the new value of the "result"
# variable. When the while loop condition becomes False (meaning
# "result" is no longer less than or equal to 50), the interpreter exits
# the loop and reads the next line of code outside of the loop. In this
# case, that next line tells the interpreter to print the string "Done".
