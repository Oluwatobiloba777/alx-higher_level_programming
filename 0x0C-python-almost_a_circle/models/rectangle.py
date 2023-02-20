#!/usr/bin/python3
""" A rectangle module """
from models.base import Base


class Rectangle(Base):
    """ A rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes attributes of a rectangle class """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Gets the width of a rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of a rectangle """
        if type(value) != int:
            raise TypeError("width must be integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ gets the height of a rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height  of a rectangle """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ gets the x value of a rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets the x vslue of a rectangle """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ gets the x value of a rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets the x vslue of a rectangle """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ it returns the area value of a rectangle """
        return self.__width * self.__height

    def display(self):
        """ it displays a rectangle with # """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """ it returns the string representation of a rectangle """
        return "[Rectangle] " \
               "({:d}) {:d}/{:d} - " \
               "{:d}/{:d}".format(self.id, self.__x, self.__y,
                                  self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ updates a rectangle """
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.width = j
                elif i == 2:
                    self.height = j
                elif i == 3:
                    self.x = j
                elif i == 4:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ it returns a dictionary representation
            of the rectangle data
        """

        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
