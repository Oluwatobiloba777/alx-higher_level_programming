#!/usr/bin/python3
""" Task 8 """


def class_to_json(obj):
    """
        a function that returns a json serialization
    """
    return obj.__dict__
