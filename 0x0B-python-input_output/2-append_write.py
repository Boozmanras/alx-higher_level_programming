#!/usr/bin/python3
"""Module to append a string to the end of a file."""


def append_write(filename="", text=""):
    """Append a string at the end of a text file (UTF8)
       and return the number of characters added.

    If the file doesn't exist, it will be created.

    Args:
        filename (str): The path to the file.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
