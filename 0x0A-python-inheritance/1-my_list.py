#!/usr/bin/python3
"""
the list module
"""


class MyList(list):
    """
    mylist class
    """

    def print_sorted(self):
        """
        returns a list sorted in ascending order
        """
        if issubclass(MyList, list):
            print(sorted(self))
