# 0x06. Python - Classes and Objects

## Description

This project is part of the ALX Higher Level Programming curriculum. It focuses on understanding and implementing object-oriented programming concepts in Python, such as classes, objects, attributes, methods, and more. The tasks require creating and managing Python classes with a focus on proper documentation and adherence to specific coding standards.

## Learning Objectives

By the end of this project, you should be able to:

- Explain why Python programming is awesome.
- Understand what a class is.
- Know how to create a class.
- Understand what an object is and how to instantiate it.
- Understand the difference between a class and an object.
- Understand what attributes are and how to add them to a class.
- Know how to use the `__init__` method.
- Understand what the `__str__` method does and how to override it.
- Understand how to compare objects using magic methods.
- Understand how to create a singly linked list.

## Project Tasks

### Task 0: My first square

- **File:** `0-square.py`
- **Description:** An empty class `Square` that defines a square.

### Task 1: Square with size

- **File:** `1-square.py`
- **Description:** A class `Square` that defines a square by its size.

### Task 2: Size validation

- **File:** `2-square.py`
- **Description:** A class `Square` that includes validation for the size attribute.

### Task 3: Area of a square

- **File:** `3-square.py`
- **Description:** A class `Square` that includes a method to calculate the area of the square.

### Task 4: Access and update private attribute

- **File:** `4-square.py`
- **Description:** A class `Square` that includes getter and setter methods for the size attribute.

### Task 5: Printing a square

- **File:** `5-square.py`
- **Description:** A class `Square` that includes a method to print the square with the `#` character.

### Task 6: Coordinates of a square

- **File:** `6-square.py`
- **Description:** A class `Square` that includes an optional position attribute to control where the square is printed.

### Task 7: Singly linked list

- **File:** `100-singly_linked_list.py`
- **Description:** A class `Node` that represents a node in a singly linked list and a class `SinglyLinkedList` to manage the list.

### Task 8: Print Square instance

- **File:** `101-square.py`
- **Description:** A class `Square` that overrides the `__str__` method to provide a string representation of the square.

### Task 9: Compare 2 squares

- **File:** `102-square.py`
- **Description:** A class `Square` that implements comparison operators based on the area of the square.

### Task 10: ByteCode -> Python #5

- **File:** `103-magic_class.py`
- **Description:** A `MagicClass` that implements a circle with methods for area and circumference, based on a provided Python bytecode.

## How to Use

Each Python file defines a class or a set of classes with specific functionalities. To test these classes, you can create instances of the classes in the Python interpreter or in a separate script.

Example:

```python
>>> from 5-square import Square
>>> my_square = Square(3)
>>> my_square.my_print()
