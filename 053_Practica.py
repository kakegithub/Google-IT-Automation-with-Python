# Convert a list to a tuple
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)

print(my_tuple)  # Outputs: (1, 2, 3, 4)

# Remember that although parentheses are often used to define a tuple,
# they're not always necessary. The following syntax is also valid:

my_tuple = 1, 2, 3, 4
print(my_tuple)  # Outputs: (1, 2, 3, 4)

#####################################################################################
# A tuple with a list as an element
my_tuple = (1, 2, ["a", "b", "c"])

# You can't change the tuple itself
# my_tuple[0] = 3  # This would raise a TypeError

# But you can modify the mutable elements within the tuple
my_tuple[2][0] = "x"
print(my_tuple)  # Outputs: (1, 2, ['x', 'b', 'c'])
######################################################################################


# Devolución de múltiples valores desde funciones
def calculate_numbers(a, b):
    return a + b, a - b, a * b, a / b


result = calculate_numbers(10, 2)
print(result)  # Outputs: (12, 8, 20, 5.0)

########################################################################################


def calculate_numbers(a, b):
    return a + b, a - b, a * b, a / b


add_result, sub_result, mul_result, div_result = calculate_numbers(10, 2)
print(add_result)  # Outputs: 12
print(sub_result)  # Outputs: 8


########################################################################################

# expresión para variable en secuencia]
my_list = [x * 2 for x in range(1, 11)]

# expresión para variable en secuencia si condición
my_list = [x for x in range(1, 101) if x % 10 == 0]

#######################################################################################

# This block of code changes the year on a list of dates.x
# The "years" list is given with existing elements.
years = [
    "January 2023",
    "May 2025",
    "April 2023",
    "August 2024",
    "September 2025",
    "December 2023",
]

# The variable "updated_years" is initialized as a list data type
# using empty square brackets []. This list will hold the new list
# with the updated years.
updated_years = []
# The for loop checks each "year" element in the list "years".
for year in years:
    # The if-statement checks if the "year" element ends with the
    # substring "2023".
    if year.endswith("2023"):
        # If True, then a temporary variable "new" will hold the
        # modified "year" element where the "2023" substring is
        # replaced with the substring "2024".
        new = year.replace("2023", "2024")
        # Then, the list "updated_years" is appended with the changed
        # element held in the temporary variable "new".
        updated_years.append(new)
    # If False, the original "year" element will be appended to the
    # the "updated_years" list unchanged.
    else:
        updated_years.append(year)

print(updated_years)
# Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]

####################################################################################################################3


# This list comprehension creates a list of squared numbers (n*n). It
# accepts two integer variables through the function’s parameters.
def squares(start, end):
    # The list comprehension calculates the square of a variable integer
    # "n", where "n" ranges from the "start" to "end" variables inclusively.
    # To be inclusive in a range(), add +1 to the end of range variable.
    return [n * n for n in range(start, end + 1)]


print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10))  # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

######################################################################################################################

# This block of code also changes the year on a list of dates using a
# different approach than demonstrated in Skill Group 1. By using a
# list comprehension, you can see how it is possible to refactor the
# code to a shorter, more efficient code block.

# The "years" list is given with existing elements.
years = [
    "January 2023",
    "May 2025",
    "April 2023",
    "August 2024",
    "September 2025",
    "December 2023",
]

# The list comprehension below creates a new list "updated_years" to
# hold the command to replace the "2023" substring of the "year"
# element with the substring "2024". This action will be executed if
# the last 4 indices of the "year" string is equal to the substring
# "2023". If false (else), the "year" element will be included in the
# new list "updated_years" unchanged.
updated_years = [
    year.replace("2023", "2024") if year[-4:] == "2023" else year for year in years
]

print(updated_years)
# Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]

########################################################################################################################33


# This function splits a given string into a list of elements. Then, it
# modifies each element by moving the first character to the end of the
# element and adds a dash between the element and the moved character.
# For example, the element "2two" will be changed to "two-2". Finally,
# the function converts the list back to a string, and returns the
# new string.
def change_string(given_string):

    # Initialize "new_string" as a string data type by using empty quotes.`
    new_string = ""

    # Split the "given_string" into a "new_list", with each "element"
    # holding an individual word from the string.
    new_list = given_string.split()

    # The for loop iterates over each "element" in the "new_list".
    for element in new_list:
        # Convert the list into a "new_string" by using the assignment
        # operator += to concatenate the following items:
        # + Each list "element" (starting at index position [1:]),
        # + a dash "-",
        # + append the first character of the "element" (using the index
        # [0]) to the end of the "element", and finally,
        # + a space " " to separate each "element" in the "new_string".
        new_string += element[1:] + "-" + element[0] + " "

    # Return the list that has been converted back into a string.
    return new_string


print(
    change_string("1one 2two 3three 4four 5five")
)  # Should print "one-1 two-2 three-3 four-4 five-5"

####################################################################################################


# This function accepts a list name and a list of elements, and returns
# a string with the format: "The "list_name" list includes: element1,
# element2, element3".
def list_elements(list_name, elements):
    # This task can be completed in a single line of code. The
    # concatenation of strings, "list_name", and the list "elements" can
    # occur on the return line. In this case, the string "The " is added
    # to the "list_name", plus the string " list includes: ", then the
    # "elements" are joined using a comma to separate each element of the
    # list.
    return "The " + list_name + " list includes: " + ", ".join(elements)


print(
    list_elements(
        "Printers", ["Color Printer", "Black and White Printer", "3-D Printer"]
    )
)
# Should print "The Printers list includes: Color Printer, Black and White Printer, 3-D Printer"

#######################################################################################################


# A simple function to add 1 to a given number
def add_one(number):
    return number + 1


# A list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map to apply the function to each element in the list
result = map(add_one, numbers)

# Convert the map object to a list to print the result
print(list(result))

# Outputs: [2, 3, 4, 5, 6]

#######################################################################################################

# Two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Use zip to combine the lists
combined = zip(names, ages)

# Convert the zip object to a list to print the result
print(list(combined))

# Outputs: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

######################################################################################################3

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.


new_filenames = []
for filename in filenames:
    if filename.endswith("hpp"):
        new = filename.replace(".hpp", ".h")
        new_filenames.append(new)
    else:
        new_filenames.append(filename)


print(new_filenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

#########################################################################################################

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
new_filenames = [
    filename.replace(".hpp", ".h") if filename.endswith(".hpp") else filename
    for filename in filenames
]  # Start your code here


print(new_filenames)
# Should print ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

########################################################################################################


def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        pig_word = word[1:] + word[0] + "ay"
        say += pig_word + " "
        # Turn the list back into a phrase
    return say.strip()


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(
    pig_latin("programming in python is fun")
)  # Should be "rogrammingpay niay ythonpay siay unfay"

#######################################################################################################


def biography_list(people):
    # Iterate over each "person" in the given "people" list of tuples.
    for person in people:

        # Separate the 3 items in each tuple into 3 variables:
        # "name", "age", and "profession"
        name, edad, profession = person

        # Format the required sentence and place the 3 variables
        # in the correct placeholders using the .format() method.
        print("{} is {} years old and works as {}".format(name, edad, profession))


# Call to the function:
biography_list(
    [("Ira", 30, "a Chef"), ("Raj", 35, "a Lawyer"), ("Maria", 25, "an Engineer")]
)


# Click Run to submit code


# Output should match:
# Ira is 30 years old and works as a Chef
# Raj is 35 years old and works as a Lawyer
# Maria is 25 years old and works as an Engineer

################################################################################################3
