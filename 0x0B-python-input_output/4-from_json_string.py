#!/usr/bin/python3
""" Task 4"""
import json


def from_json_string(my_str):
    """ a function that returns a python
        data structure represented by a JSON object
    """
    return json.loads(my_str)