# Python Inheritance Project

This project explores object-oriented programming concepts in Python, focusing on inheritance. It includes a series of classes and functions that demonstrate various aspects of inheritance and class relationships.

## Project Overview

The project consists of several Python scripts that build upon each other, starting from basic class definitions and progressing to more complex inheritance structures. Key concepts covered include:

- Class inheritance
- Method overriding
- Abstract base classes
- Attribute validation
- Special method implementation (__str__, __eq__, etc.)

## Files in the Project

1. `0-lookup.py`: Function to return list of available attributes and methods of an object
2. `1-my_list.py`: Class MyList that inherits from list
3. `2-is_same_class.py`: Function to check if an object is exactly an instance of a specified class
4. `3-is_kind_of_class.py`: Function to check if an object is an instance or inherited instance of a class
5. `4-inherits_from.py`: Function to check if an object is an inherited instance of a class
6. `5-base_geometry.py`: Empty class BaseGeometry
7. `6-base_geometry.py`: BaseGeometry class with public instance method
8. `7-base_geometry.py`: BaseGeometry class with integer validator
9. `8-rectangle.py`: Rectangle class inheriting from BaseGeometry
10. `9-rectangle.py`: Rectangle class with area() method and print() representation
11. `10-square.py`: Square class inheriting from Rectangle
12. `11-square.py`: Square class with print() representation
13. `100-my_int.py`: MyInt class inheriting from int with inverted operators
14. `101-add_attribute.py`: Function to add new attribute to an object if possible

## Usage

Each file can be run independently to test its functionality. For example:

```bash
python3 1-my_list.py
```

## Testing

Test files for some classes are provided in the `tests/` directory. Run them using the `-m doctest` option:

```bash
python3 -m doctest ./tests/*
```

## Requirements

- Python 3.8.5
- pycodestyle 2.8.*

## Author

This project is part of the ALX Higher Level Programming curriculum.
