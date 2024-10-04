#!/usr/bin/python3
"""Module to read and print the contents of a file."""


def read_file(filename=""):
    """Read a text file (UTF8) and print its contents to stdout.

    Args:
        filename (str): The path to the file to be read.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
