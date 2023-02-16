#!/usr/bin/python3
""" Task 2 """


def write_file(filename="", text=""):
    """ function that writes to a file """
    with open(filename, mode="w", encoding="utf-8") as new_file:
        return new_file.write(text)
