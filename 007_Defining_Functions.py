# functions in Python
def greeting(name):
    print("Welcome, " + name)
    
greeting("Kay")
greeting("Cameron")

#
def greeting(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)
    
greeting("Blake", "Software engineering")
greeting("Ellis", "Software engineering")

# The print() function outputs a specified object to the screen. 
month = "September"
print("Investigate failed login attempts during", month, "if more than", 100)

# The type() function returns the data type of its argument.
print(type("This is a string"))

# The str() function can be used to convert any data type to a string.
number = 12
string_representation = str(number)
print(string_representation)

# The sorted() function sorts the components of a list. 
time_list = [12, 2, 32, 19, 57, 22, 14]
print(sorted(time_list))
# The sorted() function does not change the iterable that it sorts. 
print(time_list)

# The max() function returns the largest numeric input passed into it.
# The min() function returns the smallest numeric input passed into it.
time_list = [12, 2, 32, 19, 57, 22, 14]
print(min(time_list))
print(max(time_list))




