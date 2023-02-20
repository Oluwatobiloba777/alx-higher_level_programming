#!/usr/bin/python3
""" Task 10 """


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

    def to_json(self, attrs=None):
        """
            a function that retrieves a dictionary representation
            of a student instance
        """
        result = self.__dict__
        class_d = dict()

        if type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    return result
                if i in result:
                    class_d[i] = result[i]
            return class_d
        return result
