#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    que_list = []
    for i in range(list_length):
        que = 0
        try:
            que = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            que_list.append(que)
    return que_list
