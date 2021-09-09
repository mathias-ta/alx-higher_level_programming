#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    leng = len(argv[1:])
    if leng == 0:
        print("{:d} arguments.".format(leng))
    else:
        if leng == 1:
            print("{:d} argument:".format(leng))
        else:
            print("{:d} arguments:".format(leng))
        for i, arg in enumerate(argv[1:]):
            print("{:d}: {:s}".format(i + 1, arg))
