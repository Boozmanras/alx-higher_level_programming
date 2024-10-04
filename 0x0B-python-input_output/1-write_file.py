#!/usr/bin/python3
"""Module to write a string to a file."""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and return
       the number of characters written.

    If the file doesn't exist, it will be created.
    If the file exists, its content will be overwritten.

    Args:
        filename (str): The path to the file.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
