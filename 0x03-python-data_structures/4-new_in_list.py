#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return new_list
    new_list[idx] = element
    return new_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)
print(new_list)
print(my_list)
