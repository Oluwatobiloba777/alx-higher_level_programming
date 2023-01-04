#!/usr/bin/python3
def remove_char_at(str, n):
    for a in range(len(str)):
        if (n == a):
            b = str.replace(str[n], "")
            return (b)
    else:
        return (str)
