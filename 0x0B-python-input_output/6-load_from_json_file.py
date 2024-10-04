#!/usr/bin/python3
"""Module to load a Python object from a JSON file."""

import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        any: The Python object represented by the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
