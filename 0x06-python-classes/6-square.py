#!/usr/bin/python3
"""
A module containing the square class task 4
"""


class Square:
    """
    A square class for the alx project
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the class
        Args:
            size: The size of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple \
                or value[0] < 0 \
                or value[1] < 0 \
                or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        A function to get the area of the square
        Returns:
            The area of the square (int)
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
