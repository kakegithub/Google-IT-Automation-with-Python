import math  # Importa el módulo math para utilizar la constante pi


def triangle_area(base, height):
    """
    Calcula el área de un triángulo.
    Args:
        base (float): La longitud de la base del triángulo.
        height (float): La altura del triángulo.
    Returns:
        float: El área del triángulo.
    """
    return 0.5 * base * height  # Calcula el área del triángulo


def rectangle_area(length, width):
    """
    Calcula el área de un rectángulo.
    Args:
        length (float): La longitud del rectángulo.
        width (float): El ancho del rectángulo.
    Returns:
        float: El área del rectángulo.
    """
    return length * width  # Calcula el área del rectángulo


def circle_area(radius):
    """
    Calcula el área de un círculo.
    Args:
        radius (float): El radio del círculo.
    Returns:
        float: El área del círculo.
    """
    return math.pi * radius**2  # Calcula el área del círculo utilizando la constante pi del módulo math


def donut(outside_radius, inside_radius):
    """
    Calcula el área de una dona (anillo).
    Args:
        outside_radius (float): El radio exterior de la dona.
        inside_radius (float): El radio interior de la dona.
    Returns:
        float: El área de la dona.
    """
    return circle_area(outside_radius) - circle_area(inside_radius)  # Calcula el área de la dona restando el área del círculo interior al área del círculo exterior
