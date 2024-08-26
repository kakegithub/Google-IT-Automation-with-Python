##########################################################
for x in range(5):
    print(x)
##########################################################
friends = ["Taylor", "Alex", "Pat", "Eli"]
for friend in friends:
    print("Hi " + friend)
###########################################################
values = [23, 52, 59, 37, 48]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1


print("Total sum: " + str(sum) + " - Average: " + str(sum / length))
##################################################################
product = 1
for n in range(1, 10):
    product = product * n
print(product)


#################################################################
def to_celsius(x):
    return (x - 32) * 5 / 9


for x in range(0, 101, 10):
    print(x, to_celsius(x))
#####################################################################
for n in range(1, 5, 6):
    print(n)
######################################################################
# This loop iterates on the value of the "n" variable in a range
# of 0 to 10 (the value of the end-of-range index 11 is excluded).
# The incremental value for the loop is 2. The print() function will
# output the resulting value of "n" as the loop counts from 0 to 10
# (end-of-range index 11) in incremental steps of 2. This is one
# method that can be used in Python to print a list of even numbers.


for n in range(0, 11, 2):
    print(n)


# The loop should print 0, 2, 4, 6, 8, 10
#########################################################################
# This loop iterates on the value of the "number" variable in a range
# of 2 to 7+1 (the value of the end-of-range index 7 is excluded, so
# +1 has been added to the parameter to include the numeric value 7 in
# the range). The incremental value for the loop is the default of +1.
# The print() function will output the resulting value of "number"
# multiplied by 3.


for number in range(2, 7 + 1):
    print(number * 3)


# The loop should print 6, 9, 12, 15, 18, 21
######################################################################
# This loop iterates on the value of the "x" variable in a range
# of 2 to -1 (the end-of-range index -2 is excluded). The third
# parameter is also a negative number, making it a decremental value
# of -1. The print() function will output the resulting value of
# "x" as it starts at 2 and counts down to -1 (index -2).


for x in range(2, -2, -1):
    print(x)


# The loop should print 2, 1, 0, -1
############################################################################3
