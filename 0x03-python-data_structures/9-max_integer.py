#!/usr/bin/python3
def max_integer(my_list=[]):
    leng = len(my_list)
    if leng == 0:
        return None
    else:
        maxm = my_list[0]
        for i in my_list:
            if i >= maxm:
                maxm = i
        return maxm
my_list = []
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
