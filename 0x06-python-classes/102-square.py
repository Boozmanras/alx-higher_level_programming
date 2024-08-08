#!/usr/bin/python3
"""Defines a class Square that can be compared based on area."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the square with a given size."""
        self.size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Defines the == comparison between two squares."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defines the != comparison between two squares."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Defines the < comparison between two squares."""
        return self.area() < other.area()

    def __le__(self, other):
        """Defines the <= comparison between two squares."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Defines the > comparison between two squares."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Defines the >= comparison between two squares."""
        return self.area() >= other.area()
