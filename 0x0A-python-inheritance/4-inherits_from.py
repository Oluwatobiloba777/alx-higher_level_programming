#!/usr/bin/python3
""" inherit module """


def inherits_from(obj, a_class):
    """
    checks if an object is an instance of a class inherited
    directly or indirectly
    """
    if isinstance(obj, a_class) and \
        issubclass(a_class, obj.__class__) is False:
        return True
    else:
        return False
