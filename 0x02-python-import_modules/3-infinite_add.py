#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    av = len(argv)
    sum = 0
    if av > 1:
        for i in range(1, av):
            sum += int(argv[i])
    print(sum)
