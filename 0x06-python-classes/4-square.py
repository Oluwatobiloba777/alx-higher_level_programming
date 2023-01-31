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
        self.size = size
    @property
    def size(self):
        """
        A function for the square size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        A function that sete the square size
            value: The new size of the square
        Returns:
            null
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
	def area(self):
        """
            A function that calculates the area of a sqaure
            Returns:
                The area of the square
        """
        return self.__size ** 2
