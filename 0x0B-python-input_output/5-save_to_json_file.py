#!/usr/bin/python3
"""Module to save a Python object to a file in JSON format."""

import json


def save_to_json_file(my_obj, filename):
    """Write a Python object to a text file in JSON format.

    Args:
        my_obj (any): The Python object to serialize.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
