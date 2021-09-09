#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    summ = 0
    for i, arg in enumerate(argv[1:]):
        summ = summ + int(arg)
print(summ)
