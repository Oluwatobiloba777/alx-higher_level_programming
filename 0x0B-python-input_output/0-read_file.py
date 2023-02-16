#!/usr/bin/python3
""" Task 0 """


def read_file(filename=""):
    """  function that reads a file """
    with open(filename, encoding="utf-8") as new_file:
        for line in new_file:
            print(line, end="")
