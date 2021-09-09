#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    leng = len(argv[1:])
    if leng != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    for i, arg in enumerate(argv[1:]):
        if i == 0:
            arg1 = int(arg)
        elif i == 1:
            arg2 = arg
        elif i == 2:
            arg3 = int(arg)
    if arg2 == '+':
        calc = add(arg1, arg3)
    elif arg2 == '-':
        calc = sub(arg1, arg3)
    elif arg2 == '*':
        calc = mul(arg1, arg3)
    elif arg2 == '/':
        calc = div(arg1, arg3)
    if arg2 == '+' or arg2 == '-' or arg2 == '/' or arg2 == '*':
        print("{:d} {} {:d} = {:d}".format(arg1, arg2, arg3, calc))
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
