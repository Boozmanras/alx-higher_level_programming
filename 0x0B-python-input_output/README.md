# Python Input/Output Project

## Overview
This repository contains solutions to a set of exercises and tasks that focus on Python's input and output handling. These tasks help in understanding concepts like reading from and writing to files, serialization, deserialization, Pascal’s triangle, text processing, and log parsing.

The aim is to build practical skills in managing data flow between Python programs and files while also tackling some advanced challenges.

## Directory Structure
- **0x0B-python-input_output/**  
  - `0-read_file.py`: Reads a file and prints its content to stdout.
  - `1-number_of_lines.py`: Counts the number of lines in a text file.
  - `2-read_lines.py`: Reads a specified number of lines from a text file.
  - `3-write_file.py`: Writes a string to a text file and returns the number of characters written.
  - `4-append_write.py`: Appends a string at the end of a text file.
  - `5-save_to_json_file.py`: Saves an object to a file using JSON representation.
  - `6-load_from_json_file.py`: Creates an object from a JSON file.
  - `7-add_item.py`: Adds all command line arguments to a list and saves them to a file.
  - `8-class_to_json.py`: Converts a class instance to a dictionary.
  - `9-student.py`: Defines a Student class and serializes it to JSON.
  - `10-student.py`: Extends the Student class to retrieve a filtered dictionary representation.
  - `11-student.py`: Implements a serialization and deserialization mechanism for the Student class.
  - `12-pascal_triangle.py`: Generates Pascal’s triangle.
  - `100-append_after.py`: Inserts a line of text after each line containing a specific string in a file.
  - `101-stats.py`: Parses log entries from stdin and prints statistics for each batch of 10 lines.

## Requirements
- Python 3.x
- No external libraries or modules are required; only standard Python modules are used.

## Usage

### Reading and Writing Files
- You can use scripts like `0-read_file.py` or `3-write_file.py` to perform basic operations with files, such as reading content or writing to a file.

### JSON Serialization and Deserialization
- The scripts `5-save_to_json_file.py` and `6-load_from_json_file.py` demonstrate saving Python objects to files in JSON format and restoring them.

### Pascal's Triangle
- Generate Pascal's Triangle by running:
  ```python
  python3 12-main.py
  ```
  This will print a list of lists that represent the triangle for a given value of `n`.

### Log Parsing
- To run log parsing:
  ```sh
  ./101-generator.py | ./101-stats.py
  ```
  This will generate log lines and compute metrics on file size and HTTP response codes.

## Examples
To save a student’s information to a JSON file and reload it later:

1. Create an instance of the `Student` class and convert it to JSON.
2. Save the JSON to a file using `5-save_to_json_file.py`.
3. Load the JSON data using `6-load_from_json_file.py`.
4. Use the `reload_from_json()` method to update a student object with the loaded data.

## Concepts Learned
- **File Handling**: Reading and writing to text files.
- **Serialization**: Converting data structures and class instances to JSON format.
- **Pascal’s Triangle**: Understanding recursion and list operations.
- **Log Parsing**: Processing streaming data and generating real-time metrics.

## Contributing
Feel free to contribute by forking this repository and creating pull requests for bug fixes or additional features.

## Author
- This is part of ALX software engineering foundation

