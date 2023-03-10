#!/usr/bin/python3
"""
A Square module
"""


class Square:
    """ A square class"""
    def __init__(self, size=0):
        """
        __init__ method initialize the class
        attribute:
        size: size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
