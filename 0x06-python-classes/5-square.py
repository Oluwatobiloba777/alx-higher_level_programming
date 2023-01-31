#!/usr/bin/python3
"""
A module containing the square class task 4
"""


class Square:
    """
    A square class for the alx project
    """
    def __init__(self, size=0):
        """
        Initialize the class
        Args:
            size: The size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        A function for the square size
        Returns:
            The size of the square (int)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        A function to set the square size
        Args:
            value: The new size of the square
        Returns:
            Null void
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        A function to get the area of the square
        Returns:
            The area of the square (int)
        """
        return self.__size ** 2

    def my_print(self):
        """
        A function for printing '#' squares
        Returns:
            Null Void
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print('#', end="")
                print()
