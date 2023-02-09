#!/usr/bin/python3
"""
A subclass Rectangle inheriting BaseGeometry class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    a rectangle class
    """
    def __init__(self):
        """
        instantiation of the rectangle class
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        string representation of a rectangle
        """
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
