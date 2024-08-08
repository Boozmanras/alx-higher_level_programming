# 0x08. Python - More Classes and Objects

This repository contains tasks related to Python classes and objects, focusing on concepts such as class attributes, instance methods, static methods, class methods, and more advanced features of Python's object-oriented programming (OOP). Below is a brief description of each task from the first to the tenth.

## Tasks Overview

### Task 0: Simple Rectangle
**File:** `0-rectangle.py`  
Create an empty class `Rectangle` that defines a rectangle. This serves as the foundation for building more complex functionality in subsequent tasks.

### Task 1: Real Definition of a Rectangle
**File:** `1-rectangle.py`  
Enhance the `Rectangle` class by adding private instance attributes `width` and `height`, along with property methods to retrieve and set these values with appropriate error handling.

### Task 2: Area and Perimeter
**File:** `2-rectangle.py`  
Add methods to the `Rectangle` class to calculate the area and perimeter of the rectangle. The perimeter method returns `0` if either `width` or `height` is `0`.

### Task 3: String Representation
**File:** `3-rectangle.py`  
Override the `__str__` method in the `Rectangle` class to return a string representation of the rectangle using the `#` character. This allows the rectangle to be printed in a visually meaningful way.

### Task 4: Eval is Magic
**File:** `4-rectangle.py`  
Implement the `__repr__` method in the `Rectangle` class to return a string that can recreate the rectangle using the `eval()` function. This adds support for the `repr()` function.

### Task 5: Detect Instance Deletion
**File:** `5-rectangle.py`  
Add a destructor method `__del__` to the `Rectangle` class that prints a message when an instance is deleted. This helps track when objects are removed from memory.

### Task 6: How Many Instances
**File:** `6-rectangle.py`  
Introduce a class attribute `number_of_instances` that tracks the number of instances of the `Rectangle` class. Increment this count upon instantiation and decrement it upon deletion.

### Task 7: Change Representation
**File:** `7-rectangle.py`  
Add a class attribute `print_symbol` that defines the character used for string representation. This symbol can be changed, allowing flexibility in how the rectangle is printed.

### Task 8: Compare Rectangles
**File:** `8-rectangle.py`  
Introduce a static method `bigger_or_equal` to the `Rectangle` class, which compares two rectangles and returns the one with the greater area. If they have the same area, the first rectangle is returned.

### Task 9: A Square is a Rectangle
**File:** `9-rectangle.py`  
Add a class method `square` to the `Rectangle` class that returns a new rectangle instance with equal width and height, effectively creating a square.

### Task 10: N Queens
**File:** `101-nqueens.py`  
Implement a program that solves the N Queens problem, which involves placing N non-attacking queens on an N×N chessboard. The program prints all possible solutions.

## Repository
**GitHub repository:** `alx-higher_level_programming`  
**Directory:** `0x08-python-more_classes`
