# 0x05. Python - Exceptions

## Description
This repository contains projects that demonstrate how to handle exceptions in Python.

## Files

### 0-safe_print_list.py
- Function: `def safe_print_list(my_list=[], x=0):`
- Prints `x` elements of a list.

### 1-safe_print_integer.py
- Function: `def safe_print_integer(value):`
- Prints an integer with `"{:d}".format()`.

### 2-safe_print_list_integers.py
- Function: `def safe_print_list_integers(my_list=[], x=0):`
- Prints the first `x` integers of a list.

### 3-safe_print_division.py
- Function: `def safe_print_division(a, b):`
- Divides two integers and prints the result.

### 4-list_division.py
- Function: `def list_division(my_list_1, my_list_2, list_length):`
- Divides element by element 2 lists.

### 5-raise_exception.py
- Function: `def raise_exception():`
- Raises a type exception.

### 6-raise_exception_msg.py
- Function: `def raise_exception_msg(message=""):`
- Raises a name exception with a message.

### 100-safe_print_integer_err.py
- Function: `def safe_print_integer_err(value):`
- Prints an integer and handles errors by printing to stderr.

### 101-safe_function.py
- Function: `def safe_function(fct, *args):`
- Executes a function safely.

### 102-magic_calculation.py
- Function: `def magic_calculation(a, b):`
- Bytecode to Python function conversion.

### 103-python.c
- Create three C functions that print some basic info about Python lists, Python bytes, and Python float objects.

#### Python lists:
```c
void print_python_list(PyObject *p);
