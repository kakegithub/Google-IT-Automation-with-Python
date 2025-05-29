import math


def triangle_area(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height


def rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width


def circle_area(radius):
    """Calculate the area of a circle."""
    return math.pi * radius**2


def donut(outside_radius, inside_radius):
    """Calculate the area of a donut."""
    return circle_area(outside_radius) - circle_area(inside_radius)
