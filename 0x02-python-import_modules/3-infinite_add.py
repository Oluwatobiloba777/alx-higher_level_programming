#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    av = argv - 1
    sum = 0
    for i in av:
        sum += int(i)
    print(sum)
