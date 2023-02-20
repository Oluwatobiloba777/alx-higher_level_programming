#!/usr/bin/python3
""" Task 5 """
import json


def save_to_json_file(my_obj, filename):
    """
        a function that writes json data to a file
    """
    with open(filename, mode="w", encoding="utf-8") as new_file:
        return new_file.write(json.dumps(my_obj))
