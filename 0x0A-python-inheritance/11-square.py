#!/usr/bin/python3
"""
A subclass Square inheriting Rectangle class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    a square class
    """
    def __init__(self):
        """
        instantiation of the square class
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        returns area of a square
        """
        return self.__size ** 2

    def __str__(self):
        """
        string representation of a sqaure
        """
        return '[Square]' + str(self.__size) + '/' + str(self.__size)
