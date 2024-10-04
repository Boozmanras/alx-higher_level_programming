#!/usr/bin/python3
"""Module that defines a Student class with
   JSON serialization and deserialization."""


class Student:
    """Class that represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the Student instance.

        If attrs is a list of strings, only attribute names contained in
        this list are retrieved. Otherwise, all attributes are retrieved.

        Args:
            attrs (list, optional): A list of attribute names to retrieve.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json_dict):
        """Replace all attributes of the Student
           instance with those from json_dict.

        Args:
            json_dict (dict): A dictionary containing
            attribute names and values.
        """
        for key, value in json_dict.items():
            setattr(self, key, value)
