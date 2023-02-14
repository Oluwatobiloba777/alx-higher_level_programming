#!/usr/bin/python3
""" Task 9 """


class Student:
    """
        a student class
    """
    def __init__(self, first_name, last_name, age):
        """
            initialization of attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            a function that retrieves a dictionary representation
            of a student instance
        """
        return self.__dict__