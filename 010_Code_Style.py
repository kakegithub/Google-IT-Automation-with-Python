# Calculation of the area of ​​a circle(bad style)
def calculate(d):
    q = 3.14
    z = q * (d ** 2)
    print(z)

calculate(5) #Output is 78.5


# Calculation of the area of ​​a circle(good style)
def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)

circle_area(5) #Output is 78.5