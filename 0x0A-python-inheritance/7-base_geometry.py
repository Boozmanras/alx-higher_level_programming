#!/usr/bin/python3
"""
This module contains the BaseGeometry class with
area and integer_validator methods.
"""


class BaseGeometry:
    """
    A class representing base geometry with area
    and integer validator methods.
    """

    def area(self):
        """
        Raises an Exception with the message
       'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer greater than 0.

        Args:
            name (str): The name of the value.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
