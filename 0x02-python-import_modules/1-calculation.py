#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    sum = add(a, b)
    dif = sub(a, b)
    pro = mul(a, b)
    que = div(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, sum))
    print("{:d} - {:d} = {:d}".format(a, b, dif))
    print("{:d} * {:d} = {:d}".format(a, b, pro))
    print("{:d} / {:d} = {:d}".format(a, b, que))
