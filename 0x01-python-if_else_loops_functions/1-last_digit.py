#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
	rem = number % 10
else:
	rem = number % (-10)

if rem > 5:
	print("Last digit of {:d} is {:d} and is greater then 5".format(number, rem))
if rem == 0:
	print("Last digit of {:d} is 0 and is 0".format(number))
if rem < 6 and rem != 0:
	print("last digit of {:d} is {:d} and is less than 6 and not 0".format(number, rem))
