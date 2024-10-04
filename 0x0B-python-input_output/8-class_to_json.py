#!/usr/bin/python3
"""Module to convert a class instance to a
   dictionary for JSON serialization."""


def class_to_json(obj):
    """Return the dictionary description of a class instance.

    Args:
        obj (object): The class instance to convert.

    Returns:
        dict: A dictionary containing the class attributes.
    """
    return obj.__dict__
