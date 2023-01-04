#!/usr/bin/python3
def uppercase(str):
    for a in str:
        b = ord(a)
        if (96 < b < 123):
            b = b - 32
        print("{:c}".format(b), end="")
    print(end='\n')
