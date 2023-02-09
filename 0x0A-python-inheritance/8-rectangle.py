#!/usr/bin/python3
"""
A subclass Rectangle inheriting BaseGeometry class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    a rectangle class
    """
    def __init__(self, width, height):
        """
        instantiation of the rectangle class
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
