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

    def integer_validator(self, name, value):
        """
        it checks an integer value
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
