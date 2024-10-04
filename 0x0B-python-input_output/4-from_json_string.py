#!/usr/bin/python3
"""Module to convert a JSON string to a Python object."""

import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        any: The Python object represented by `my_str`.
    """
    return json.loads(my_str)
