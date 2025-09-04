# --- Crear una instancia de una clase ---
class Apple:
    """
    Representa una manzana con un color y un sabor.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de la clase Apple.
        Por defecto, el color es rojo y el sabor es dulce.
        """
        self.color = "red"
        self.flavor = "sweet"


honeycrisp = Apple()  # Crea una instancia de la clase Apple
print(honeycrisp.color)  # Imprime el color de la manzana honeycrisp
# red

# --- Modificar variables ---
class Apple:
    """
    Representa una manzana con un color y un sabor.
    """

    def __init__(self, color, flavor):
        """
        Inicializa una nueva instancia de la clase Apple con un color y un sabor específicos.
        Args:
            color (str): El color de la manzana.
            flavor (str): El sabor de la manzana.
        """
        self.color = color
        self.flavor = flavor


honeycrisp = Apple("red", "sweet")  # Crea una instancia de Apple con color rojo y sabor dulce
fuji = Apple("red", "tart")  # Crea una instancia de Apple con color rojo y sabor ácido

print(honeycrisp.flavor)  # Imprime el sabor de la manzana honeycrisp
print(fuji.flavor)  # Imprime el sabor de la manzana fuji
# sweet
# tart

# --- Otros métodos especiales ---
class Apple:
    """
    Representa una manzana con un color y un sabor.
    """

    def __init__(self, color, flavor):
        """
        Inicializa una nueva instancia de la clase Apple con un color y un sabor específicos.
        Args:
            color (str): El color de la manzana.
            flavor (str): El sabor de la manzana.
        """
        self.color = color
        self.flavor = flavor

    def __str__(self):
        """
        Devuelve una representación en cadena de la manzana.
        Returns:
            str: Una cadena que describe el color y el sabor de la manzana.
        """
        return "An apple which is {} and {}".format(self.color, self.flavor)


honeycrisp = Apple("red", "sweet")  # Crea una instancia de Apple con color rojo y sabor dulce
print(honeycrisp)  # Imprime la representación en cadena de la manzana honeycrisp
# prints "An apple which is red and sweet"

class Apple:
    """
    Representa una manzana con un color y un sabor.
    """

    def __init__(self, color, flavor):
        """
        Inicializa una nueva instancia de la clase Apple con un color y un sabor específicos.
        Args:
            color (str): El color de la manzana.
            flavor (str): El sabor de la manzana.
        """
        self.color = color
        self.flavor = flavor


jonagold = Apple("red", "sweet")  # Crea una instancia de Apple con color rojo y sabor dulce
print(jonagold.color)  # Imprime el color de la manzana jonagold

class Apple:
    """
    Representa una manzana con un color y un sabor.
    """

    def __init__(self, color, flavor):
        """
        Inicializa una nueva instancia de la clase Apple con un color y un sabor específicos.
        Args:
            color (str): El color de la manzana.
            flavor (str): El sabor de la manzana.
        """
        self.color = color
        self.flavor = flavor

    def __str__(self):
        """
        Devuelve una representación en cadena de la manzana.
        Returns:
            str: Una cadena que describe el color y el sabor de la manzana.
        """
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)


jonagold = Apple("red", "sweet")  # Crea una instancia de Apple con color rojo y sabor dulce
print(jonagold)  # Imprime la representación en cadena de la manzana jonagold

# --- Ejemplo de clase Piglet ---
class Piglet:
    """
    Representa un cerdito con un nombre y una edad.
    """

    years = 0
    name = "piglet"

    def speak(self):
        """
        Imprime un mensaje con el nombre del cerdito.
        """
        print("Oink! I'm {}! oink".format(self.name))

    def pig_years(self):
        """
        Calcula la edad del cerdito en años de cerdo.
        Returns:
            int: La edad del cerdito en años de cerdo.
        """
        return self.years * 18


hamlet = Piglet()  # Crea una instancia de la clase Piglet
hamlet.name = "Hamlet"  # Asigna el nombre "Hamlet" al cerdito hamlet
hamlet.speak()  # El cerdito hamlet dice su nombre

petunia = Piglet()  # Crea una instancia de la clase Piglet
petunia.name = "Petunia"  # Asigna el nombre "Petunia" al cerdito petunia
petunia.speak()  # El cerdito petunia dice su nombre

piggy = Piglet()  # Crea una instancia de la clase Piglet
piggy.name = "Piggy"  # Asigna el nombre "Piggy" al cerdito piggy
piggy.years = 2  # Asigna la edad 2 al cerdito piggy
print(piggy.pig_years())  # Imprime la edad del cerdito piggy en años de cerdo

# --- Ejemplo de clase Triangle ---
class Triangle:
    """
    Representa un triángulo con una base y una altura.
    """

    def __init__(self, base, height):
        """
        Inicializa una nueva instancia de la clase Triangle con una base y una altura específicas.
        Args:
            base (float): La longitud de la base del triángulo.
            height (float): La altura del triángulo.
        """
        self.base = base
        self.height = height

    def area(self):
        """
        Calcula el área del triángulo.
        Returns:
            float: El área del triángulo.
        """
        return 0.5 * self.base * self.height

    def __add__(self, other):
        """
        Anula el operador + para "sumar" dos triángulos.
        Args:
            other (Triangle): El otro triángulo a sumar.
        Returns:
            float: La suma de las áreas de los dos triángulos.
        """
        return self.area() + other.area()


triangle1 = Triangle(10, 5)  # Crea una instancia de Triangle con base 10 y altura 5
triangle2 = Triangle(6, 8)  # Crea una instancia de Triangle con base 6 y altura 8

print("The area of triangle 1 is :", triangle1.area())  # Imprime el área del triángulo 1
print("The area of triangle2 is :", triangle2.area())  # Imprime el área del triángulo 2
print(
    "The area of both triangles is :", triangle1 + triangle2
)  # Imprime la suma de las áreas de los dos triángulos

# --- Definición de clases y métodos ---
# class ClassName:
#     def method_name(self, others_parameters):
#         #body_of_method
