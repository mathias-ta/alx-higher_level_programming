#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    if roman_string == "":
        return 0
    num = 0
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i, j in zip(roman_string, roman_string[1:]):
        if i not in dic.keys():
            return 0
        elif dic[i] >= dic[j]:
            num += dic[i]
        else:
            num -= dic[i]
    num += dic[roman_string[-1]]
    return num
"""
def roman_to_int(roman_string):
    rom_str = roman_string[::-1]
    c_num = 0
    p_num = 0
    t_int = 0
    if roman_string is None or type(roman_string) is not str:
        return 0
    if roman_string == "":
        return 0
    if rom_str is not None:
        for char in rom_str:
            if ord(char) == ord("I"):
                c_num = 1
            elif ord(char) == ord("V"):
                c_num = 5
            elif ord(char) == ord("X"):
                c_num = 10
            elif ord(char) == ord("L"):
                c_num = 50
            elif ord(char) == ord("C"):
                c_num = 100
            elif ord(char) == ord("D"):
                c_num = 500
            elif ord(char) == ord("M"):
                c_num = 1000
            else:
                return 0
            if c_num < p_num:
                c_num = c_num * -1
            t_int = t_int + c_num
            p_num = c_num
        return t_int
    return 0
"""
