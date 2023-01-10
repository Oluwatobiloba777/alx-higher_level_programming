#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    max_int = min(my_list)
    for i in my_list:
        if i > max_int:
            max_int = i

    return max_int
