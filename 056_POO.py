# Crear una instancia de una clase
class apple:
    def __init__(self):
        self.color = "red"
        self.flavor = "sweet"


honeycrisp = apple()
print(honeycrisp.color)

# red
###############################################

# Modificar variables


class apple:
    def __init(self):
        self.color = "red"
        self.flavor = "sweet"


# honeycrisp = apple("red", "sweet")
# fuji = apple("red", "tart")

# print(honeycrisp.flavor)
# print(fuji.flavor)

# sweet , tart

#######################################################3
# Otros métodos especiales


class apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "an apple which  is {} and {} ".format(self.color, self.flavor)


honeycrisp = apple("red", "sweet")
print(honeycrisp)

# prints "an apple which is red and sweet"

###########################################################################


class apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor


jonagold = apple("red", "sweet")
print(jonagold.color)


#############################################################################


class apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)


jonagold = apple("red", "sweet")
print(jonagold)

#######################################################################################


class Piglet:
    years = 0
    name = "piglet"

    def speak(self):
        print("Oink! I'm {}! oink".format(self.name))

    def pig_years(self):
        return self.years * 18


hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()

piggy = Piglet()
piggy.name = "Piggy"
piggy.years = 2
print(piggy.pig_years())

######################################################################################


class Triangle:
    # a clase Triangle tiene un método __init__()que se llama constructor y se utiliza para inicializar los atributos del objeto.
    def __init__(self, base, height):
        self.base = base
        self.height = height

    # calcula el área del triángulo basándose en su altura y longitud de la base.
    def area(self):
        return 0.5 * self.base * self.height

    # Este método anula el operador + para "sumar" dos triángulos.
    def __add__(self, other):
        return self.area() + other.area()


triangle1 = Triangle(10, 5)
triangle2 = Triangle(6, 8)

print("The area of triangle 1 is :", triangle1.area())
print("The area of triangle2 is :", triangle2.area())
print("The area of both triangles is :", triangle1 + triangle2)

#################################################################################


# Definición de clases y métodos
# class ClassName:
#     def method_name(self, others_parameters):
#         #body_of_method


####################################################################################3
