#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [] 
    if my_list is not None:
        for i in my_list:
            if i == search:
                new_list.append(replace)
            else:
                new_list.append(i)
        return new_list
    return None
