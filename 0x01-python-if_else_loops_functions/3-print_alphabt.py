#!/usr/bin/python3
for char in range(ord("a"), ord("z") + 1):
    print("{}".format(chr(char)), end="")
    if char == ord("e") or char == ord("q"):
        print("\b", end="")
