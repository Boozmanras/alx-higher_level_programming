#!/usr/bin/python3
"""Defines a class Square with a private size attribute."""

class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initializes the square with a given size.
        
        Args:
            size (int): The size of the square.
        """
        self.__size = size
