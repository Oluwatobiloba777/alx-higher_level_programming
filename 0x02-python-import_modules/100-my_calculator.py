#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
     av = len(argv) - 1

    if av == 3:
        operator = argv[2]
        num1 = int(argv[1])
        num2 = int(argv[3])
        if operator == '+':
            result = add(num1, num2)
            print('{:d} + {:d} = {:d}'.format(num1, num2, result))
            exit(0)
        elif operator == '-':
            result = sub(num1, num2)
            print('{:d} - {:d} = {:d}'.format(num1, num2, result))
            exit(0)
        elif operator == '*':
            result = mul(num1, num2)
            print('{:d} * {:d} = {:d}'.format(num1, num2, result))
            exit(0)
        elif operator == '/':
            result = div(num1, num2)
            print('{:d} / {:d} = {:d}'.format(num1, num2, result))
            exit(0)
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
    else:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
