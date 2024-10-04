#!/usr/bin/python3
"""
This module contains the MyInt class that inherits from int.
"""


class MyInt(int):
    """
    A class representing a rebel integer with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Inverts the == operator.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
