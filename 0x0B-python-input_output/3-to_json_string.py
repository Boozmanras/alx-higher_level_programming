#!/usr/bin/python3
"""Module to convert a Python object to its JSON string representation."""

import json


def to_json_string(my_obj):
    """Return the JSON representation of a Python object.

    Args:
        my_obj (any): The Python object to serialize.

    Returns:
        str: JSON string representation of `my_obj`.
    """
    return json.dumps(my_obj)
