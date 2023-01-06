#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if (len(argv) - 1 != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        num1 = int(argv[1])
        num2 = int(argv[3])
        if (argv[2] == '+'):
            if (len(argv) - 1 >= 3):
                print("{} + {} = {}".format(num1, num2, (add(num1, num2))))
                exit(0)
        if (argv[2] == '-'):
            if (len(argv) - 1 >= 3):
                print("{} - {} = {}".format(num1, num2, (sub(num1, num2))))
                exit(0)
        if (argv[2] == '*'):
            if (len(argv) - 1 >= 3):
                print("{} * {} = {}".format(num1, num2, (mul(num1, num2))))
                exit(0)
        if (argv[2] == '/'):
            if (len(argv) - 1 >= 3):
                print("{} / {} = {}".format(num1, num2, (div(num1, num2))))
                exit(0)
        if (argv[2] != '+', '-', '*', '/'):
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
