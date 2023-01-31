#!/usr/bin/python3
"""
A Square module
"""

class Square:
    """ A square class"""
    def __init__(self, size, position=(0, 0)):
        """
        __init__ method initialize the class
        attribute:
        size: size of the square
        """
        self.size = size
        self.position = position
	@property
    def size(self):
        """
        A function of the square size
        Returns:
             size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        A function that sets the square size
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
    @property
    def position(self):
        return self.position

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
            A function that calculates the area of a sqaure
            Returns:
                The area of the square
        """
        return self.__size ** 2
	def my_print(self):
        """
        A function that prints # squares
        Returns:
            null
        """
        if self.__size == 0:
            print()
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

