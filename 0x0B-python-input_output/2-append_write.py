#!/usr/bin/python3
""" Task 2 """


def append_write(filename="", text=""):
    """ a function that appends to a file"""
    with open(filename, mode="a", encoding="utf-8") as new_file:
        return new_file.write(text)
