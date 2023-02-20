#!/usr/bin/python3
""" A square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ initializes the atrributes of a square """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ it returns the string representation of a square """
        return "[Square] ({:d}) " \
               "{:d}/{:d} - {:d}".format(self.id,
                                        self.x,
                                        self.y,
                                        self.width)

    @property
    def size(self):
        """ returns the size of a square """
        return self.height

    @size.setter
    def size(self, value):
        """ sets the size of a square """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updates a sqaure """
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                elif i == 3:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
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
            "size": self.size,
            "x": self.x,
            "y": self.y
        }