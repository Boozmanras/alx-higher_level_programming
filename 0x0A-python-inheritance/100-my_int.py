#!/usr/bin/python3
"""Module for MyInt class."""

class MyInt(int):
    """A rebel integer class with inverted == and != operators."""

    def __eq__(self, other):
        """Invert the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert the != operator."""
        return super().__eq__(other)
