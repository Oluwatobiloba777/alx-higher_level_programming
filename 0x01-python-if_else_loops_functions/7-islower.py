#!/usr/bin/python3
def islower(c):
    lower_char = ord(c)
    if lower_char > 96 and lower_char < 123:
        return True
    else:
        return False
