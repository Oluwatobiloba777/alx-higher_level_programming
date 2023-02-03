#!/usr/bin/python3
""" A rectangle module """


class Rectangle:
    """ A rectangle Class """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ this method initializes the attributes """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ this method(getter) returns the width of a rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ this method(setter) for the width of a rectangle """

        if type(value) != int:
            raise TypeError ("width must be an integer")
        elif width < 0:
            raise ValueError ("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ this method(getter) returns for the height of a rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ this method(setter) for the height of a rectangle """

        if type(value) != int:
            raise TypeError ("height must be an integer")
        elif height < 0:
            raise ValueError ("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ this method returns the area of a rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ this method returns the perimeter of a rectangle """

        if self.__width or self.__height == 0:
            return 0
        else:
            2 * (self.__height + self.__width)

    def __str__(self):
        """ this method returns the string representation of a rectangle """
        new_string = ""
        if not (self.__width == 0 or self.__height == 0):
            for i in range(self.__height):
                new_string += f"{self.print_symbol}" * self.__width
                if i != (self.__height - 1):
                    new_string += '\n'
        return new_string

    def __repr__(self):
        """ this method returns canonical representation of a rectangle """
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """ this method prints a message after an instance is deleted """
        print ("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ this method returns the bigger rectangle """
        if rect_1 != Rectangle:
            raise TypeError ("rect_1 must be an instance of Rectangle")
        if rect_2 != Rectangle:
            raise TypeError ("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """ this method returns a new rectangle instance with width ==
        height == size """
        return cls(size, size)
