#!/usr/bin/python3
""" inherit module """


def inherits_from(obj, a_class):
    """
    checks if an object is an instance of a class inherited
    directly or indirectly
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
