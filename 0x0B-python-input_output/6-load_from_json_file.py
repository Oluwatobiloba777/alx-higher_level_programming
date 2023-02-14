#!/usr/bin/python3
""" Task 6 """
import json


def load_from_json_file(filename):
    """
        a function that loads json data to a file
    """
    with open(filename, encoding="utf-8") as new_file:
        return json.load(new_file)