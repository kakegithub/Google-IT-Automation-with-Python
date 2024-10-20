# Documentación de clases, métodos y funciones
class ClassName:
    """Documentacion for the class"""

    def method_name(self, other_parameters):
        """Documentacion para el metodo"""
        body_of_method  # type: ignore

    def function_name(parameters):
        """Documentacion de la funcion"""
        body_of_parameters  # type: ignore


########################################################################################
def my_function(x):
    """
    Sample usage:
    >>> my_function(“example input”)
    "example output"
    """


########################################################################################
# En una sección interactiva de Python, puedes mostrar docstrings con:
# help(some_function)

##########################################################################################

# some_function.__doc__
# print(some_function.__doc__)
# function_explanation = other_function.__doc__
##########################################################################################
