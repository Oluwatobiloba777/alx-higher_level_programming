#!/usr/bin/python3
""" Task 0 """


def read_file(filename=""):
    """  function that reads a file """
    with open(filename, mode="r", encoding="utf-8") as new_file:
        line = new_file.read()
        print(line, end="")
