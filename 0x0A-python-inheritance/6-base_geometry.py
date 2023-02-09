#!/usr/bin/python3
"""
A BaseGeometry module
"""


class BaseGeometry:
    """
    A BaseGeometry class
    """

    def area(self):
        """
        returns an exception if area is not implemented
        """
        raise Exception('area() is not implemented')
