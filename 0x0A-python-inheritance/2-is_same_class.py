#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    checks if obj is an instance of a specified class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
