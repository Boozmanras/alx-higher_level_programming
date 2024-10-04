#!/usr/bin/python3
"""
Module for text indentation.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = text.replace(delim, delim + "\n\n")

    lines = [line.strip() for line in text.split("\n")]
    formatted_text = "\n".join(line for line in lines if line)
    print(formatted_text, end="")
