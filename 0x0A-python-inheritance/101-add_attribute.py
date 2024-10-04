#!/usr/bin/python3
"""
This module contains a function that adds a
new attribute to an object if possible.
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: The object to add the attribute to.
        attr (str): The name of the attribute to add.
        value: The value of the attribute to add.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
