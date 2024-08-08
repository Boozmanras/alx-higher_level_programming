#!/usr/bin/python3
import math

class MagicClass:
    """Represents a class that mimics the given bytecode."""

    def __init__(self, radius=0):
        """Initializes the MagicClass with a radius.
        
        Args:
            radius (float or int): The radius of the circle.
        
        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0
        if type(radius) not in [int, float]:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference of the circle."""
        return 2 * math.pi * self.__radius
