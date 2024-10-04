#!/usr/bin/python3
class MyList(list):
    """
    A class that inherits from list and provides additional functionality.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))
