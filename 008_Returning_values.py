# Calculating the area of triangulo
def area_triangle(base, height):
    return base*height/2

# Sum of the areas of a triangle
area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))

# Calculate time in hours minutes and seconds given the seconds
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
 
hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

# Function that displays a greeting on the screen
def greeting(name):
    print("Welcome, " + name)
result = greeting("Christine")
print(result)
